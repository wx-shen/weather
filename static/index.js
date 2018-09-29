	$(function(){

		//建立图表
		function Createchart(ydata,dname,ceilling){
			var chart = Highcharts.chart('chart-container', {
			    title: {
			        text: '气候网站'+dname+'数据'
			    },
			     credits: {
		            enabled: false
		        },
			    yAxis: {
			        title: {
			            text: dname
			        },
			        plotLines:[{
	                color:'red',            //线的颜色，定义为红色
	                dashStyle:'solid',     //默认是值，这里定义为长虚线
	                value:ceilling,         //定义在那个值上显示标示线，这里是在x轴上刻度为3的值处垂直化一条线
	                width:2,               //标示线的宽度，2px
	                label:{
	                    text:'警戒线',     //标签的内容
	                    align:'left',                //标签的水平位置，水平居左,默认是水平居中center
	                    x:10,                         //标签相对于被定位的位置水平偏移的像素，重新定位，水平居左10px
	                    style:{
	                        fontSize:'14px',
	                        fontWeight:'bold'
	                    }
	                }
			    }]
			},
			    plotOptions: {
			        series: {
			        	color:Highcharts.getOptions().colors[2],
			            label: {
			                connectorAllowed: false
			            },
			            series:{
			            	lineWidth: 1,
			            	shadow: false,
			            	marker: {
	                            radius: 1,
	                            states: {
	                                hover: {
	                                    radius: 2
	                                }
	                            }
	                        },
			            }
			            //pointStart: 2010
			        }
			    },
			    tooltip:{
			    	backgroundColor:'rgba(255,255,255,0.7)'

			    },
			    series: [{
			        name: dname,
			        data: ydata
			    }],
			});

		}

            	
		$("#btncheck").bind("click",function(){

            var preurl = "http://127.0.0.1:9001/weather/58238/";
		    var option=$('#SelectData option:selected');
		    var selectdata=option.val();
		    var optiontext=option.text();
		    var ceildata=$('#ceilling').val();
		    // console.log(selectdata);

			// 显示发送的url
            var myurl=preurl+selectdata+'/0';
			$("#urltext")
			.empty()
			.append(myurl);
			// 向后台服务器发送请求
			$.ajax({
				method:'GET',
				url:myurl,
				dataType:"text",
				success:function(result){
					console.log(result);
					$("#dataResult")
					.empty()
					.append(result);				
			        //处理json数据
			        var myarr=[];
			        var numArray =JSON.parse(result)
			        console.log(numArray);
			        Createchart(numArray,optiontext,ceildata);
			    }
			});
			$.ajax({
				method:'GET',
				url:'http://127.0.0.1:9001/58665',
				dataType:"text",
				success:function(result){
//					 console.log(result);
					 info=JSON.parse(result)[0];
					 lon=info['longitude'];
					 lai=info['latitude'];
					 name=info['name'];
					 sid=info['sid'];
					 time=info['updatetime'];
					 $('#longitude').val(lon);
					 $('#latitude').val(lai);
					 $('#sid').val(sid);
					 $('#name').val(name);
					 $('#updatetime').val(time);


			    }
			});
		     
		})
	});