import { NestFactory } from '@nestjs/core';
import { AppModule } from './app.module';
import { join } from 'path';
import * as hbs from 'hbs';
import { NestExpressApplication } from '@nestjs/platform-express';
import { DocumentBuilder, SwaggerModule } from '@nestjs/swagger';
import { winstonLogger } from '../utils/winston.util';

async function bootstrap() {
  const app = await NestFactory.create<NestExpressApplication>(AppModule,{
    logger:winstonLogger,
  });

  // Enable CORS
  app.enableCors();

  const viewsPath = join(__dirname, '..', 'views');
  app.setBaseViewsDir(viewsPath);
  app.setViewEngine('hbs');
  hbs.registerPartials(join(viewsPath, 'partials'));

  const config = new DocumentBuilder()
    .setTitle('For Test')
    .setDescription('testing nestjs application')
    .setVersion('1.0')
    .addBearerAuth(
      {
        type: 'http',
        scheme: 'bearer',
        name: 'JWT',
        in: 'header',
      },
      'access-token',
    )
    .build();

  const document = SwaggerModule.createDocument(app, config);
  SwaggerModule.setup('api', app, document);

  await app.listen(3000);
}
bootstrap();
