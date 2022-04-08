function saveFile() {
    var inValue = {
        Criminals: document.querySelector('#person').value,
        Gender: document.querySelector('#gender').value,
        Ethnicity: document.querySelector('#nationality').value,
        Birthplace: document.querySelector('#hometown').value,
        Accusation: document.querySelector('#cause').value,
        Courts: document.querySelector('#courts').value,
        Verb: document.querySelector('#verb').value,
        Adj: document.querySelector('#adj').value,
        Time: document.querySelector('#time').value
    }
    var jsonstr = JSON.stringify(inValue);
    exportRaw("标注——" + document.querySelector('#person').value, jsonstr);
}

function exportRaw(name, data) {
    var urlObject = window.URL || window.webkitURL || window;
    var export_blob = new Blob([data]);
    var save_link = document.createElementNS("http://www.w3.org/1999/xhtml", "a")
    save_link.href = urlObject.createObjectURL(export_blob);
    save_link.download = name;
    fakeClick(save_link);
}

function fakeClick(obj) {
    var ev = document.createEvent("MouseEvents");
    ev.initMouseEvent("click", true, false, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null);
    obj.dispatchEvent(ev);
}