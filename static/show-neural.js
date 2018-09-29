

//使用go easy,对数据进行监听
var goEasy = new GoEasy({
appkey: "BC-45bbf8e0213d40ea943c439dd7389caa"
});
goEasy.subscribe({
channel:'demo_channel',
onMessage: function(message){
info=JSON.parse(message.content)  //接受自后端的JSON数组，[[i,jw],[w0,w1,w2,...]]
chart.series[0].addPoint(info[0]);
var str1= '第'+info[0][0]+'次训练';
var j='代价：'+info[0][1];
$("#time").html(str1);
$("#jw").html(j);
for(var i=0;i<7;i++){
    var idname='#w'+i;
    var str='w'+i+': '+info[1][i];
    $(idname).html(str);
}
//console.log(info[1]);

   }
});


var chart = Highcharts.chart('container1', {
			    title: {
			        text: 'J(w)'
			    },
			     credits: {
		            enabled: false
		        },
			    yAxis: {
			        title: {
			            text: 'J(w)'
			        },
			        plotLines:[{
	                color:'red',            //线的颜色，定义为红色
	                dashStyle:'solid',     //默认是值，这里定义为长虚线
	                value:0,         //定义在那个值上显示标示线，这里是在x轴上刻度为3的值处垂直化一条线
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
			        name: '差距',
			        data: [[]]
			    }],
			});


