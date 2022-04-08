var obj1
var obj2
var url1 = "/templates/json/keyword.json"/*json文件url，本地的就写本地的位置，如果是服务器的就写服务器的路径*/
var request1 = new XMLHttpRequest();
request1.open("get", url1);/*设置请求方法与路径*/
request1.send(null);/*不发送数据到服务器*/
request1.onload = function () {/*XHR对象获取到返回信息后执行*/
    if (request1.status == 200) {/*返回状态为200，即为数据获取成功*/
        obj1 = JSON.parse(request1.responseText);
    }
}
var url2 = "/templates/json/partsofspeech.json"
var request2 = new XMLHttpRequest();
request2.open("get", url2);/*设置请求方法与路径*/
request2.send(null);/*不发送数据到服务器*/
request2.onload = function () {/*XHR对象获取到返回信息后执行*/
    if (request2.status == 200) {/*返回状态为200，即为数据获取成功*/
        obj2 = JSON.parse(request2.responseText);
    }
}

function personshow() {
    var x = obj1["当事人"][0];
    var s = $('#person').val();
    if (s.length == 0) {
        s += x;
    } else if (s.indexOf(x) == -1) {
        s += "、" + x;
    }
    $('#person').val(s);
}

function gendershow() {
    var x = obj1["性别"][0];
    var s = $('#gender').val();
    if (s.length == 0) {
        s += x;
    } else if (s.indexOf(x) == -1) {
        s += "、" + x;
    }
    $('#gender').val(s);
}

function nationalityshow() {
    var x = obj1["民族"][0];
    var s = $('#nationality').val();
    if (s.length == 0) {
        s += x;
    } else if (s.indexOf(x) == -1) {
        s += "、" + x;
    }
    $('#nationality').val(s);
}

function hometownshow(a) {
    var x = obj1["地名"];
    var s = $('#hometown').val();
    if (s.length == 0) {
        s += x[a];
    } else if (s.indexOf(x[a]) == -1) {
        s += "、" + x[a];
    }
    $('#hometown').val(s);
}

function causeshow() {
    var x = obj1["案由"];
    var s = $('#cause').val();
    if (s.length == 0) {
        s += x;
    } else if (s.indexOf(x) == -1) {
        s += "、" + x;
    }
    $('#cause').val(s);
}

function courtsshow(a) {
    var x = obj1["相关法院"];
    var s = $('#courts').val();
    if (s.length == 0) {
        s += x[a];
    } else if (s.indexOf(x[a]) == -1) {
        s += "、" + x[a];
    }
    $('#courts').val(s);
}
function verbshow(a) {
    var x = obj2["动词"];
    var s = $('#verb').val();
    if (s.length == 0) {
        s += x[a];
    } else if (s.indexOf(x[a]) == -1) {
        s += "、" + x[a];
    }
    $('#verb').val(s);
}
function adjshow(a) {
    var x = obj2["形容词"];
    var s = $('#adj').val();
    if (s.length == 0) {
        s += x[a];
    } else if (s.indexOf(x[a]) == -1) {
        s += "、" + x[a];
    }
    $('#adj').val(s);
}
function timeshow(a) {
    var x = obj2["时间词"];
    var s = $('#time').val();
    if (s.length == 0) {
        s += x[a];
    } else if (s.indexOf(x[a]) == -1) {
        s += "、" + x[a];
    }
    $('#time').val(s);
}
