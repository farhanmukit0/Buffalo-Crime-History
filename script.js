function ajaxGetRequest(path, callback){
    let request = new XMLHttpRequest();
    request.onreadystatechange = function(){
        if (this.readyState === 4 && this.status === 200){
            callback(this.response);
        }
    };
    request.open("GET", path);
    request.send();
}

function ajaxPostRequest(path, data, callback){
    let request = new XMLHttpRequest();
    request.onreadystatechange = function(){
        if (this.readyState === 4 && this.status === 200){
            callback(this.response);
        }
    };
    request.open("POST", path);
    request.send(data);
}

function showBarChart(r){
  let data = JSON.parse(r);
  console.log(r);
  let years = [];
  for (let i in data) {
    years.push(i);
  }
  let num = [];
  for (let n in data){
    num.push(data[n]);
  }
  let bardata = [{x:years,y:num,type:'bar'}];
  var layout = {
  title: 'Incidents by Year',
  xaxis: {
    title: 'Year',
  },
  yaxis: {
    title: 'Number of Incidents',
  }};  
  Plotly.newPlot('bar', bardata, layout);
}

function showPieChart(r){
  let data = JSON.parse(r);
  console.log(r);
  let days = [];
  for (let i in data) {
    days.push(i);
  }
  let num = [];
  for (let n in data){
    num.push(data[n]);
  }
  let piedata = [{values:num,labels:days,type:'pie'}];
  var layout = {
  title: 'Incidents by Day of the Week'
  };  
  Plotly.newPlot('pie', piedata, layout);
}

function showLineChart(r){
  let data = JSON.parse(r);
  let h = document.getElementById('hour').value
  let list = [];
  let dict = {};
  for (let i of data){
    if (i[2] === h){
      dict[i[0]] = 0;
    }
  }
  for (let j of data){
    for (let m in dict){
      if (j[2] === h && j[0] === m){
        dict[m] += 1;
      }
    }
  }
  newdict = {}
  for (let k in dict) {
    if (dict[k] > 20) {
      newdict[k] = dict[k]
    }
  }
  let years = [];  
  for (let m in newdict) {
    years.push(m);
  }
  let num = [];
  for (let m in newdict){
    num.push(newdict[m]);
  }
  var linedat = [{x:years,y:num,type:'scatter'}];
  var layout = {
  title: ('Incidents at ' + h + ' hundred hours'),
  xaxis: {
    title: 'Year',
  },
  yaxis: {
    title: 'Number of Incidents',
  }}; 
  Plotly.newPlot('line',linedat, layout)
}

function getData(){
  ajaxGetRequest('/barchart', showBarChart);
  ajaxGetRequest('/piechart', showPieChart)
}

function getHourData(){
  ajaxPostRequest("/linechart",hour,showLineChart)
}