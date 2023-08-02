import os
from minio import Minio
from minio.error import S3Error
from config import MINIO_address, MINIO_access_key, MINIO_secret_key
from datetime import timedelta


class MinioHelper():
    def __init__(self):
        self.bucket_name = None
        self.client = Minio(
            MINIO_address,
            access_key=MINIO_access_key,
            secret_key=MINIO_secret_key,
            secure=False,
        )

    def set_bucket(self, bucket_name):
        try:
            self.bucket_name = bucket_name
            if not self.client.bucket_exists(bucket_name):
                self.client.make_bucket(bucket_name)
            print('complete set bucket')
                
        except S3Error as err:
            print(err)
           
    def delete_bucket(self, bucket_name):
        try:
            # delete all objects in bucket
            objects = self.client.list_objects(bucket_name)
            for obj in objects:
                self.client.remove_object(bucket_name, obj.object_name)
            
            # delete bucket
            self.client.remove_bucket(bucket_name)
            print(f"Bucket '{bucket_name}' has been deleted.")

        except Exception as e:
            print(f"Error deleting bucket '{bucket_name}': {e}")  
            
    def process_image(self, img_path, minio_id, category):
        try:
            meta_data = {"category": category}
            result = self.client.fput_object(
                self.bucket_name, minio_id, img_path, metadata=meta_data
            )

            print(
                "created {0} object; etag: {1}".format(
                    result.object_name, result.etag
                ),
            )

        except S3Error as err:
            print(err)

    def get_url(self, minio_id): #minio id 이용해서 이미지 찾기 -> url 찾기 -> url로 milvus에서 이미지로 만들어서 디코딩 -> search -> minio id 반환
        #milvus에 저장되는 id를 minio id로 저장
        try:
            data_url = self.client.presigned_get_object(self.bucket_name, minio_id, expires=timedelta(hours=1))
            
            return data_url
                
        except S3Error as err:
            print(f"error: {err}")
            
    def get_image(self, bucket_name, minio_id):
        try:
            data = self.client.get_object(bucket_name, minio_id)
            script_dir = os.path.dirname(os.path.abspath(__file__))
            os.chdir(script_dir)

            save_path = os.path.join(script_dir,'results', str(os.path.basename(minio_id))+'.JPEG')
            os.makedirs(os.path.dirname(save_path), exist_ok=True)

            with open(save_path, "wb") as file:
                file.write(data.read())
                
        except S3Error as err:
            print(f"error: {err}")
            
if __name__ == '__main__':
    min = MinioHelper()
    BUCKET_NAME = 'baseimages'
    min.delete_bucket(BUCKET_NAME)