<script lang="ts">
	import { onMount } from 'svelte';
	import { Tabs, TabItem } from 'flowbite-svelte';
	import { chart } from 'svelte-apexcharts';
	// import ApexCharts from 'apexcharts';
	export let data;

	let ApexCharts: any;

	let areaChart1: HTMLElement | null = null;
	let areaChart2: HTMLElement | null = null;
	let areaChart3: HTMLElement | null = null;

	let donutChart1: HTMLElement | null = null;
	let columnChart1: HTMLElement | null = null;
	let canRender = false;

	const loadApexCharts = async () => {
		const module = await import('apexcharts');
		ApexCharts = module.default;
	};

	// Chart for visitors
	let lineoptions = {
		chart: {
			type: 'area',
			height: '300%',
			width: '100%',
			background: '#fff',
			animations: {
				enabled: true,
				easing: 'easeinout',
				speed: 800,
				animateGradually: {
					enabled: true,
					delay: 150
				}
			}
		},

		colors: ['#4FC0D0', '#E91E63', '#9C27B0'],
		series: [
			{
				name: 'visit',
				data: [4, 5, 6, 5, 7, 6, 7]
			}
		],
		xaxis: {
			categories: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'],
			style: {
				colors: [],
				fontSize: '20px',
				fontFamily: 'Helvetica, Arial, sans-serif',
				fontWeight: 500,
				cssClass: 'apexcharts-xaxis-label'
			}
		},
		title: {
			text: 'Visitors this week',
			align: 'center',
			margin: 10,
			offsetX: 0,
			offsetY: 0,
			floating: false,
			style: {
				fontSize: '26px',
				fontWeight: 'bold',
				fontFamily: undefined,
				color: '#263238'
			}
		},
		grid: {
			show: true
		}
	};

	const getChartOptions = () => {
		return {
			series: [60, 30, 10],
			colors: ['#18777D', '#2E8A99', '#4FC0D0'],
			chart: {
				height: 420,
				width: '100%',
				type: 'pie'
			},
			stroke: {
				colors: ['white'],
				lineCap: ''
			},
			plotOptions: {
				pie: {
					labels: {
						show: true
					},
					size: '100%',
					dataLabels: {
						offset: -25
					}
				}
			},
			labels: ['Direct', 'Organic search', 'Others'],
			dataLabels: {
				enabled: true,
				style: {
					fontFamily: 'Inter, sans-serif'
				}
			},
			legend: {
				position: 'bottom',
				fontFamily: 'Inter, sans-serif'
			},
			yaxis: {
				labels: {
					formatter: function (value) {
						return value + '%';
					}
				}
			},
			xaxis: {
				labels: {
					formatter: function (value) {
						return value + '%';
					}
				},
				axisTicks: {
					show: false
				},
				axisBorder: {
					show: false
				}
			}
		};
	};

	// ApexCharts options and config
	let signupoption = {
		series: [
			{
				name: 'Organic',
				color: '#85E6C5',
				data: [
					{ x: 'Mon', y: 1 },
					{ x: 'Tue', y: 1 },
					{ x: 'Wed', y: 2 },
					{ x: 'Thu', y: 1 },
					{ x: 'Fri', y: 2 },
					{ x: 'Sat', y: 1 },
					{ x: 'Sun', y: 1 }
				]
			},
			
		],
		chart: {
			type: 'bar',
			height: '320px',
			fontFamily: 'Inter, sans-serif',
			toolbar: {
				show: false
			}
		},
		plotOptions: {
			bar: {
				horizontal: false,
				columnWidth: '70%',
				borderRadiusApplication: 'end',
				borderRadius: 8
			}
		},
		tooltip: {
			shared: true,
			intersect: false,
			style: {
				fontFamily: 'Inter, sans-serif'
			}
		},
		states: {
			hover: {
				filter: {
					type: 'darken',
					value: 1
				}
			}
		},
		stroke: {
			show: true,
			width: 0,
			colors: ['transparent']
		},
		grid: {
			show: false,
			strokeDashArray: 4,
			padding: {
				left: 2,
				right: 2,
				top: -14
			}
		},
		dataLabels: {
			enabled: false
		},
		legend: {
			show: false
		},
		xaxis: {
			floating: false,
			labels: {
				show: true,
				style: {
					fontFamily: 'Inter, sans-serif',
					cssClass: 'text-xs font-normal fill-gray-500 dark:fill-gray-400'
				}
			},
			axisBorder: {
				show: false
			},
			axisTicks: {
				show: false
			}
		},
		yaxis: {
			show: false
		},
		fill: {
			opacity: 1
		}
	};

	let hoptions = {
      series: [
        {
          name: "Income",
          color: "#93B1A6",
          data: ["10", "10", "10", "10", "10", "10"],
        },
      ],
      chart: {
        sparkline: {
          enabled: false,
        },
        type: "bar",
        width: "100%",
        height: 400,
        toolbar: {
          show: false,
        }
      },
      fill: {
        opacity: 1,
      },
      plotOptions: {
        bar: {
          horizontal: true,
          columnWidth: "100%",
          borderRadiusApplication: "end",
          borderRadius: 6,
          dataLabels: {
            position: "top",
          },
        },
      },
      legend: {
        show: true,
        position: "bottom",
      },
      dataLabels: {
        enabled: false,
      },
      tooltip: {
        shared: true,
        intersect: false,
        formatter: function (value) {
          return  value
        }
      },
      xaxis: {
        labels: {
          show: true,
          style: {
            fontFamily: "Inter, sans-serif",
            cssClass: 'text-xs font-normal fill-gray-500 dark:fill-gray-400'
          },
          formatter: function(value) {
            return value
          }
        },
        categories: ["Bearing", "Robotics", "Sensors", "Shaft", "Ball", "Roller"],
        axisTicks: {
          show: false,
        },
        axisBorder: {
          show: false,
        },
      },
      yaxis: {
        labels: {
          show: true,
          style: {
            fontFamily: "Inter, sans-serif",
            cssClass: 'text-xs font-normal fill-gray-500 dark:fill-gray-400'
          }
        }
      },
      grid: {
        show: true,
        strokeDashArray: 4,
        padding: {
          left: 2,
          right: 2,
          top: -20
        },
      },
      fill: {
        opacity: 1,
      }
    }


	onMount(async () => {
		await loadApexCharts();
		canRender = true;

		let options = {
			chart: {
				height: '250px',
				maxWidth: '100%',
				type: 'area',
				fontFamily: 'Inter, sans-serif',
				dropShadow: {
					enabled: false
				},
				toolbar: {
					show: false
				}
			},
			tooltip: {
				enabled: true,
				x: {
					show: false
				}
			},
			fill: {
				type: 'gradient',
				gradient: {
					opacityFrom: 0.55,
					opacityTo: 0,
					shade: '#1C64F2',
					gradientToColors: ['#1C64F2']
				}
			},
			dataLabels: {
				enabled: false
			},
			stroke: {
				width: 6
			},
			grid: {
				show: false,
				strokeDashArray: 4,
				padding: {
					left: 2,
					right: 2,
					top: 0
				}
			},
			series: [
				{
					name: 'New users',
					data: [4, 8, 6, 12, 9, 16],
					color: '#1A56DB'
				}
			],
			xaxis: {
				categories: [
					'01 February',
					'02 February',
					'03 February',
					'04 February',
					'05 February',
					'06 February',
					'07 February'
				],
				labels: {
					show: false
				},
				axisBorder: {
					show: false
				},
				axisTicks: {
					show: false
				}
			},
			yaxis: {
				show: false
			}
		};

		if (document.getElementById('pie-chart') && typeof ApexCharts !== 'undefined') {
			const chart = new ApexCharts(document.getElementById('pie-chart'), getChartOptions());
			chart.render();
		}

		if (areaChart1 && typeof ApexCharts !== 'undefined') {
			const chart1 = new ApexCharts(areaChart1, getChartOptions);
			chart1.render();
		}

		if (areaChart2 && typeof ApexCharts !== 'undefined') {
			const chart2 = new ApexCharts(areaChart2, signupoption);
			chart2.render();
		}

		if (areaChart3 && typeof ApexCharts !== 'undefined') {
			const chart3 = new ApexCharts(areaChart3, hoptions);
			chart3.render();
		}
	});
</script>

<article>
	<div class="m-20">
		<h1 class="mb-4 text-3xl font-extrabold text-gray-900 dark:text-white md:text-5xl lg:text-6xl">
			<span class="text-transparent bg-clip-text bg-gradient-to-r to-emerald-600 from-sky-500"
				>Xsearch</span
			> Statistics
		</h1>
		<p class="text-lg font-normal text-gray-500 lg:text-xl dark:text-gray-400">
			It showed the number of weekly visitors to the web service, the route of user inflow, the
			number of newly added data, the number of subscribers, and the user search record.
		</p>
	</div>

<!-- C -->
<div class="bg-gray-50 p-5">
	<div class="text-sm text-gray-500 dark:text-gray-400 m-10">
		<div class=" w-full bg-white rounded-lg shadow dark:bg-gray-800 p-4">
			<section>
				<div use:chart={lineoptions} />
			</section>
		</div>
	</div>
</div>

<!-- Donut Chart -->
<div class=" flex-wrap md:m-5">
	<div id='explorer' style="width: calc(33.33% - 12px);">
	<div
		class="w-full bg-white rounded-lg shadow dark:bg-gray-800 p-4 md:p-6 m-10 md:m-5"
	>
		<div class="flex justify-between items-start w-full">
			<div class="flex-col items-center">
				<div class="flex items-center mb-1">
					<div>
						<h5 class="leading-none text-3xl font-bold text-gray-900 dark:text-white pb-2">
							User Inflow Path
						</h5>
						<p class="text-base font-normal text-gray-500 dark:text-gray-400">
							Percentage of User Inflow Paths
						</p>
					</div>
				</div>
			</div>
		</div>

		<div class="py-6" id="pie-chart" />

		<!-- mini chart Table -->
		<div
			class="grid grid-cols-1 items-center border-gray-200 border-b dark:border-gray-700 justify-between"
		/>
		<div class="flex justify-between items-center pt-5" />
		<table class="w-full text-sm text-left text-gray-500 dark:text-gray-400">
			<thead class="text-xs text-gray-700 uppercase bg-gray-50 dark:bg-gray-700 dark:text-gray-400">
				<tr>
					<th scope="col" class="px-6 py-3"> Top Channels </th>
					<th scope="col" class="px-6 py-3"> Users </th>
					<th scope="col" class="px-6 py-3"> Percentage </th>
				</tr>
			</thead>
			<tbody>
				<tr class="bg-white border-b dark:bg-gray-900 dark:border-gray-700">
					<th
						scope="row"
						class="px-6 py-4 font-medium text-gray-900 whitespace-nowrap dark:text-white"
					>
						Direct
					</th>
					<td class="px-6 py-4"> 6 </td>
					<td class="px-6 py-4">
						<div class="w-full bg-gray-200 rounded-full dark:bg-gray-700">
							<div
								class="bg-green-600 text-xs font-medium text-blue-100 text-center p-0.5 leading-none rounded-full"
								style="width: 60%"
							>
								60%
							</div>
						</div>
					</td>
				</tr>
				<tr class="border-b bg-gray-50 dark:bg-gray-800 dark:border-gray-700">
					<th
						scope="row"
						class="px-6 py-4 font-medium text-gray-900 whitespace-nowrap dark:text-white"
					>
						Organic Search
					</th>
					<td class="px-6 py-4"> 3 </td>
					<td class="px-6 py-4">
						<div class="w-full bg-gray-200 rounded-full dark:bg-gray-700">
							<div
								class="bg-green-600 text-xs font-medium text-blue-100 text-center p-0.5 leading-none rounded-full"
								style="width: 30%"
							>
								30%
							</div>
						</div>
					</td>
				</tr>
				<tr class="border-b bg-gray-50 dark:bg-gray-800 dark:border-gray-700">
					<th
						scope="row"
						class="px-6 py-4 font-medium text-gray-900 whitespace-nowrap dark:text-white"
					>
						Other
					</th>
					<td class="px-6 py-4"> 1 </td>
					<td class="px-6 py-4">
						<div class="w-full bg-gray-200 rounded-full dark:bg-gray-700">
							<div
								class="bg-green-600 text-xs font-medium text-blue-100 text-center p-0.5 leading-none rounded-full"
								style="width: 10%"
							>
								10%
							</div>
						</div>
					</td>
				</tr>
			</tbody>
		</table>
	</div>
</div>

<div id="main">
<div id="sub1" 
class="flex">
	<div
		class="w-full bg-white rounded-lg shadow dark:bg-gray-800 p-4 md:p-6 m-0 md:m-5"
		>
		<div class="flex justify-between">
			<div>
				<h5 class="leading-none text-3xl font-bold text-gray-900 dark:text-white pb-2">
					Sign Up
				</h5>
				<p class="text-base font-normal text-gray-500 dark:text-gray-400">Number of Signup</p>
			</div>
			<div
				class="flex items-center px-2.5 py-0.5 text-base font-semibold text-green-500 dark:text-green-500 text-center"
			>
				1%
				<svg
					class="w-3 h-3 ml-1"
					aria-hidden="true"
					xmlns="http://www.w3.org/2000/svg"
					fill="none"
					viewBox="0 0 10 14"
				>
					<path
						stroke="currentColor"
						stroke-linecap="round"
						stroke-linejoin="round"
						stroke-width="2"
						d="M5 13V1m0 0L1 5m4-4 4 4"
					/>
				</svg>
			</div>
		</div>
		<div bind:this={areaChart2} />
	</div>

	<div
		class="w-full bg-white rounded-lg shadow dark:bg-gray-800 p-4 md:p-6 m-0 md:m-5"
	>
		<div class="flex justify-between">
			<div>
				<h5 class="leading-none text-3xl font-bold text-gray-900 dark:text-white pb-2">Data Type</h5>
				<p class="text-base font-normal text-gray-500 dark:text-gray-400">Number of Data by Type</p>
			</div>
			
		</div>
		<div bind:this={areaChart3} />
	</div>
</div>

<!-- Table -->
<div id="sub2">
	<div
		class="grid grid-cols-1 items-center border-gray-200 border-t dark:border-gray-700 justify-between"
	/>

	<h3 class="text-3xl font-bold dark:text-white m-10 md:m-5">Search history</h3>

	<div class="relative overflow-x-auto shadow-md sm:rounded-lg md:m-5">
		<table class="w-full text-sm text-left text-gray-500 dark:text-gray-400">
			<thead class="text-xs text-gray-700 uppercase bg-gray-50 dark:bg-gray-700 dark:text-gray-400">
				<tr>
					<th scope="col" class="px-6 py-3"> Id </th>
					<th scope="col" class="px-6 py-3"> Category </th>
					<th scope="col" class="px-6 py-3"> Score </th>
					<th scope="col" class="px-6 py-3"> Timestamp </th>
				</tr>
			</thead>
			<tbody>
				<tr class="bg-white border-b dark:bg-gray-900 dark:border-gray-700">
					<th
						scope="row"
						class="px-6 py-4 font-medium text-gray-900 whitespace-nowrap dark:text-white"
					>
						User1
					</th>
					<td class="px-6 py-4"> Bearing </td>
					<td class="px-6 py-4"> 0.95 </td>
					<td class="px-6 py-4"> 2023-08-21 10:23:45 </td>
				</tr>
				<tr class="border-b bg-gray-50 dark:bg-gray-800 dark:border-gray-700">
					<th
						scope="row"
						class="px-6 py-4 font-medium text-gray-900 whitespace-nowrap dark:text-white"
					>
						User2
					</th>
					<td class="px-6 py-4"> Ball </td>
					<td class="px-6 py-4"> 0.72 </td>
					<td class="px-6 py-4"> 2023-08-21 11:45:23 </td>
				</tr>
				<tr class="bg-white border-b dark:bg-gray-900 dark:border-gray-700">
					<th
						scope="row"
						class="px-6 py-4 font-medium text-gray-900 whitespace-nowrap dark:text-white"
					>
						User3
					</th>
					<td class="px-6 py-4"> Bearing </td>
					<td class="px-6 py-4"> 0.87 </td>
					<td class="px-6 py-4"> 2023-08-21 14:32:19 </td>
				</tr>
				<tr class="border-b bg-gray-50 dark:bg-gray-800 dark:border-gray-700">
					<th
						scope="row"
						class="px-6 py-4 font-medium text-gray-900 whitespace-nowrap dark:text-white"
					>
						User4
					</th>
					<td class="px-6 py-4"> Robotics </td>
					<td class="px-6 py-4"> 0.98 </td>
					<td class="px-6 py-4"> 2023-08-21 16:54:01 </td>
				</tr>
			</tbody>
		</table>
	</div>
</div>
</div>
</div>
</article>

<footer class="bg-white rounded-lg shadow m-4 dark:bg-gray-800">
	<div class="w-full mx-auto max-w-screen-xl p-4 md:flex md:items-center md:justify-between">
		<span class="text-sm text-gray-500 sm:text-center dark:text-gray-400"
			>© 2023 <a href="#" class="hover:underline">Xsearch</a>. All Rights Reserved.
		</span>
		<ul
			class="flex flex-wrap items-center mt-3 text-sm font-medium text-gray-500 dark:text-gray-400 sm:mt-0"
		>
			<li>
				<a href="#" class="mr-4 hover:underline md:mr-6">About</a>
			</li>
			<li>
				<a href="#" class="mr-4 hover:underline md:mr-6">Privacy Policy</a>
			</li>
			<li>
				<a href="#" class="mr-4 hover:underline md:mr-6">Licensing</a>
			</li>
			<li>
				<a href="#" class="hover:underline">Contact</a>
			</li>
		</ul>
	</div>
</footer>

<style>
	h1,
	h3,
	p {
		margin: 20px;
	}
	.flex-wrap {
		display: flex;
		flex-wrap: wrap;
	}
	article{
		flex-basis: 680px;
    flex-grow: 1;
    flex-shrink: 1;
    background-color: #ffffff;
	}


#explorer {
    display: flex;
    flex-grow: 2;
    flex-direction: column;
    margin: 10px;
    padding: 3px;
}
#main {
    display: flex;
    flex-grow: 8;
    flex-direction: column;
    margin: 10px;
    padding: 3px;
}


</style>