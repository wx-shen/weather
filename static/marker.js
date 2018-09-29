
 //站点信息
 var lnglats= [["114.17","22.31"],["125.23","49.16"],["128.90","47.71"],
["126.76","45.75"],["88.08","47.73"],["87.62","43.78"],
["82.95","41.71"],["75.98","39.46"],["88.16","39.03"],
["79.93","37.13"],["82.71","37.06"],["97.03","41.80"],
["94.68","40.15"],["103.08","38.63"],["94.90","36.41"],
["98.10","36.30"],["104.15","35.87"],["111.68","40.81"],
["107.40","40.76"],["106.21","38.48"],["112.55","37.78"],
["109.50","36.60"],["106.66","35.55"],["129.46","42.88"],
["123.43","41.76"],["126.91","41.71"],["116.28","39.93"],
["117.55","36.70"],["120.33","36.06"],["92.06","31.48"],
["91.13","29.66"],["102.90","35.00"],["100.00","31.61"],
["103.83","30.70"],["102.26","27.90"],["104.28","26.86"],
["102.68","25.01"],["103.38","23.38"],["113.65","34.71"],
["107.03","33.06"],["108.97","34.43"],["112.58","33.03"],
["109.46","30.28"],["111.30","30.70"],["114.13","30.61"],
["106.48","29.51"],["113.08","28.20"],["110.00","27.56"],
["106.65","26.48"],["110.30","25.33"],["113.03","25.80"],
["114.95","25.85"],["117.15","34.28"],["120.25","33.76"],
["115.73","32.86"],["118.80","32.00"],["121.46","31.40"],
["117.05","30.53"],["120.16","30.23"],["115.91","28.60"],
["121.41","28.61"],["117.46","27.33"],["119.28","26.08"],
["121.51","25.03"],["118.08","24.48"],["106.60","23.90"],
["111.30","23.48"],["113.05","23.66"],["116.66","23.35"],
["108.21","22.63"],["110.35","20.03"]];
    var data = [
        {"id":45004,"name":"KingsPark","type":1},
        {"id":50557,"name":"Nenjiang","type":1},
        {"id":50774,"name":"Yichun","type":1},
        {"id":50953,"name":"Harbin","type":1},
        {"id":51076,"name":"Altay","type":1},
        {"id":51463,"name":"Urumqi ","type":1},
        {"id":51644,"name":"Kuqa ","type":1},
        {"id":51709,"name":"Kashi ","type":1},
        {"id":51777,"name":"Ruoqiang ","type":1},
        {"id":51828,"name":"Hotan ","type":1},
        {"id":51839,"name":"Minfeng ","type":1},
        {"id":52323,"name":"Mazong Shan","type":1},
        {"id":52418,"name":"Dunhuang ","type":1},
        {"id":52681,"name":"Minqin","type":1},
        {"id":52818,"name":"Golmud","type":1},
        {"id":52836,"name":"Dulan","type":1},
        {"id":52983,"name":"YuZhong","type":1},
        {"id":53463,"name":"Hohhot","type":1},
        {"id":53513,"name":"Linhe","type":1},
        {"id":53614,"name":"Yinchuan","type":1},
        {"id":53772,"name":"Taiyuan","type":1},
        {"id":53845,"name":"Yanan","type":1},
        {"id":53915,"name":"Pingliang","type":1},
        {"id":54292,"name":"Yanji","type":1},
        {"id":54342,"name":"Shenyang","type":1},
        {"id":54374,"name":"Linjiang","type":1},
        {"id":54511,"name":"Beijing","type":1},
        {"id":54727,"name":"Zhangqiu","type":1},
        {"id":54857,"name":"Qingdao","type":1},
        {"id":55299,"name":"Nagqu ","type":1},
        {"id":55591,"name":"Lhasa ","type":1},
        {"id":56080,"name":"Hezuo","type":1},
        {"id":56146,"name":"Garze","type":1},
        {"id":56187,"name":"Wenjiang","type":1},
        {"id":56571,"name":"Xichang","type":1},
        {"id":56691,"name":"Weining","type":1},
        {"id":56778,"name":"Kunming","type":1},
        {"id":56985,"name":"Mengzi","type":1},
        {"id":57083,"name":"Zhengzhou","type":1},
        {"id":57127,"name":"Hanzhong","type":1},
        {"id":57131,"name":"Jinghe","type":1},
        {"id":57178,"name":"Nanyang","type":1},
        {"id":57447,"name":"Enshi","type":1},
        {"id":57461,"name":"Yichang","type":1},
        {"id":57494,"name":"Wuhan","type":1},
        {"id":57516,"name":"Chongqing","type":1},
        {"id":57679,"name":"Changsha","type":1},
        {"id":57749,"name":"Huaihua","type":1},
        {"id":57816,"name":"Guiyang","type":1},
        {"id":57957,"name":"Guilin","type":1},
        {"id":57972,"name":"Chenzhou","type":1},
        {"id":57993,"name":"Ganzhou","type":1},
        {"id":58027,"name":"Xuzhou","type":1},
        {"id":58150,"name":"Sheyang","type":1},
        {"id":58203,"name":"Fuyang","type":1},
        {"id":58238,"name":"Nanjing","type":1},
        {"id":58362,"name":"Shanghai","type":1},
        {"id":58424,"name":"Anqing","type":1},
        {"id":58457,"name":"Hangzhou","type":1},
        {"id":58606,"name":"Nanchang","type":1},
        {"id":58665,"name":"Hongjia","type":1},
        {"id":58725,"name":"Shaowu","type":1},
        {"id":58847,"name":"Fuzhou","type":1},
        {"id":58968,"name":"Taibei","type":1},
        {"id":59134,"name":"Xiamen","type":1},
        {"id":59211,"name":"Baise","type":1},
        {"id":59265,"name":"Wuzhou","type":1},
        {"id":59280,"name":"Qingyuan","type":1},
        {"id":59316,"name":"Shantou","type":1},
        {"id":59431,"name":"Nanning","type":1},
        {"id":59758,"name":"Haikou","type":1}
        ];
  var myurl='http://127.0.0.1:9001/weather/warning/1';
  var aurl='http://127.0.0.1:9001/weather/warning/2';
 // var myurl='http://127.0.0.1:9000/weather/warning/1';
 //  var aurl='http://127.0.0.1:9000/weather/warning/2';
  var map = new AMap.Map("container", {});
   function get_warning(){
       $.ajax({
                    method:'GET',
                    url:myurl,
                    dataType: "text",
                    success:function(result){

                        var jobj=JSON.parse(result);
                        run(jobj);

                    },
                    error:function(){
                         console.log('error get!')
                    }
                });
              }

   get_warning();

function run(jobj){
    for(var i= 0;i<lnglats.length;i++){
    //addMarker();
    //添加marker标记
    function addMarker(infoWin) {
        if(jobj[data[i].id]==1) //温度告警
        {
            var marker = new AMap.Marker({
                map: map,
                position:  lnglats[i],
                title: data[i].id,
                icon: 'static/images/11.png'
            });
        }
        else if(jobj[data[i].id]==0) //无告警
        {
            var marker = new AMap.Marker({
                    map: map,
                    position:  lnglats[i],
                    title: data[i].id,
                    icon: 'static/images/0.png'
                });
        }
        else if(jobj[data[i].id]==3) //双重告警
        {
            var marker = new AMap.Marker({
                        map: map,
                        position:  lnglats[i],
                        title: data[i].id,
                        icon: 'static/images/1.png'
                    });
        }
         else if(jobj[data[i].id]==-1) //数据未更新告警
        {
            var marker = new AMap.Marker({
                        map: map,
                        position:  lnglats[i],
                        title: data[i].id,
                        icon: 'static/images/01.png'
                    });
        }
        else  //风速告警,使用默认标记点
        {
            var marker = new AMap.Marker({
                    map: map,
                    position:  lnglats[i],
                    title: data[i].id
                });
        }
        //鼠标点击marker弹出自定义的信息窗体
        AMap.event.addListener(marker, 'click', function() {
            infoWin.open(map, marker.getPosition()); //打开窗口
            show_info_charts(marker.getTitle()); //显示图表
        });
    }

    //实例化信息窗体
    var title = data[i].id,
        content = [];
    content.push("站点名称："+data[i].name);
    content.push("<a href='http://127.0.0.1:9000/"+title+"'>站点天气详情</a>");
    var infoWin = new AMap.InfoWindow({
        isCustom: true,  //使用自定义窗体
        content: createInfoWindow(title, content.join("<br/>")),
        offset: new AMap.Pixel(16, -45)
    });
    addMarker(infoWin);
    }

}

  //构建自定义信息窗体
    function createInfoWindow(title, content) {
        var info = document.createElement("div");
        info.className = "info";

        //可以通过下面的方式修改自定义窗体的宽高
        //info.style.width = "400px";
        // 定义顶部标题
        var top = document.createElement("div");
        var titleD = document.createElement("div");
        var closeX = document.createElement("img");
        top.className = "info-top";
        titleD.innerHTML = title;
        closeX.src = "http://webapi.amap.com/images/close2.gif";
        closeX.onclick = closeInfoWindow;

        top.appendChild(titleD);
        top.appendChild(closeX);
        info.appendChild(top);

        // 定义中部内容
        var middle = document.createElement("div");
        middle.className = "info-middle";
        middle.style.backgroundColor = 'white';
        middle.innerHTML = content;
        info.appendChild(middle);

        // 定义底部内容
        var bottom = document.createElement("div");
        bottom.className = "info-bottom";
        bottom.style.position = 'relative';
        bottom.style.top = '0px';
        bottom.style.margin = '0 auto';
        var sharp = document.createElement("img");
        sharp.src = "http://webapi.amap.com/images/sharp.png";
        bottom.appendChild(sharp);
        info.appendChild(bottom);
        return info;
    }


    //关闭信息窗体
    function closeInfoWindow() {
        map.clearInfoWindow();
    }

      //添加多边形覆盖物
 function addPolygon(){
   var polygonArr=new Array();//多边形覆盖物节点坐标数组
   polygonArr.push(new AMap.LngLat("118.80","32.00"));
   polygonArr.push(new AMap.LngLat("121.46","31.40"));
   polygonArr.push(new AMap.LngLat("120.16","30.23"));
   polygonArr.push(new AMap.LngLat("117.05","30.53"));
   polygon=new AMap.Polygon({
   path:polygonArr,//设置多边形边界路径
   strokeColor:"#87CEEB", //线颜色
   strokeOpacity:0.2, //线透明度
   strokeWeight:3,    //线宽
   fillColor: "#FF6347", //填充色
   fillOpacity: 0.35//填充透明度
  });
   polygon.setMap(map);
 }


 //告警区域隐藏
 function clear_area(){
    var overlaysList = map.getAllOverlays('circle');
    for(var i=0;i<overlaysList.length;i++)
    {
        overlaysList[i].setMap(null);
    }
    //console.log(overlaysList);

 }



 //添加圆覆盖物
function addCircle() {
    $.ajax({
                    method:'GET',
                    url:aurl,
                    dataType: "text",
                    success:function(result){

                        var wpos=JSON.parse(result);
                         for(var i=0;i<wpos.length;i++ ){
                               circle = new AMap.Circle({
                               center:new AMap.LngLat(wpos[i][0],wpos[i][1]),// 圆心位置
                               radius:80000, //半径
                               strokeColor: "#F33", //线颜色
                               strokeOpacity: 1, //线透明度
                               strokeWeight: 3, //线粗细度
                               fillColor: "#ee2200", //填充颜色
                               fillOpacity: 0.35//填充透明度
                               });
                               circle.setMap(map);
                              }


                    },
                    error:function(){
                         console.log('error get!')
                    }
                });

}


//显示站点highcharts图表信息
function Createchart(ydata,dname,ceilling,container){
			var chart = Highcharts.chart(container, {
			    title: {
			        text: '站点高空'+dname+'数据'
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
function show_info_charts(sid){
		var tempurl="http://127.0.0.1:9001/weather/"+sid+"/temp/0";
		var drcturl="http://127.0.0.1:9001/weather/"+sid+"/drct/0";
		var sknturl="http://127.0.0.1:9001/weather/"+sid+"/sknt/0";
		var presurl="http://127.0.0.1:9001/weather/"+sid+"/pres/0";
		 $.ajax({
                    method:'GET',
                    url:tempurl,
                    dataType: "text",
                    success:function(result){

                        console.log(result);
                        var numArray=JSON.parse(result);
                        optiontext='温度';
                        ceildata=-70;
                        Createchart(numArray,optiontext,ceildata,'chart-container1');

                    },
                    error:function(){
                         console.log('error get!')
                    }
                });

                $.ajax({
                    method:'GET',
                    url:sknturl,
                    dataType: "text",
                    success:function(result){

                        console.log(result);
                        var numArray=JSON.parse(result);
                        optiontext='风速';
                        ceildata=70;
                        Createchart(numArray,optiontext,ceildata,'chart-container2');

                    },
                    error:function(){
                         console.log('error get!')
                    }
                });

                $.ajax({
                    method:'GET',
                    url:presurl,
                    dataType: "text",
                    success:function(result){

                        console.log(result);
                        var numArray=JSON.parse(result);
                        optiontext='气压';
                        ceildata=2000;
                        Createchart(numArray,optiontext,ceildata,'chart-container3');

                    },
                    error:function(){
                         console.log('error get!')
                    }
                });

                $.ajax({
                    method:'GET',
                    url:drcturl,
                    dataType: "text",
                    success:function(result){

                        console.log(result);
                        var numArray=JSON.parse(result);
                        optiontext='风向';
                        ceildata=0;
                        Createchart(numArray,optiontext,ceildata,'chart-container4');

                    },
                    error:function(){
                         console.log('error get!')
                    }
                });

            }