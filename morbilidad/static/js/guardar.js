var options = {
  valueNames: [ 'enfermedad', 'masculino', 'femenino', 'total', 'mes', 'ano',]
};

var consultaList = new List('consultas', options);

function handleFiles(files) {
	// Check for the various File API support.
	if (window.FileReader) {
		// FileReader are supported.
		getAsText(files[0]);
	} else {
		alert('FileReader are not supported in this browser.');
	}
}

function getAsText(fileToRead) {
	var reader = new FileReader();
	// Handle errors load
	reader.onload = loadHandler;
	reader.onerror = errorHandler;
	// Read file into memory as UTF-8
	reader.readAsText(fileToRead, 'ISO-8859-1');
}

function loadHandler(event) {
	var csv = event.target.result;
	processData(csv);
}

function processData(csv) {
    var allTextLines = csv.split(/\r\n|\n/);
    var lines = [];
    while (allTextLines.length) {
        lines.push(allTextLines.shift().split(','));
    }
	drawOutput(lines);
}

function errorHandler(evt) {
	if(evt.target.error.name == "NotReadableError") {
		alert("No se puede leer el archivo");
	}
}

function drawOutput(lines){
	for(var i=0; i<lines.length; i++) {
	
	    $('#alldata').append('<tr><td width="294" class="enfermedad"><div contenteditable>'+lines[i][0]+'</div></td><td width="172" class="masculino"><div contenteditable>'+lines[i][1]+'</div></td><td width="172" class="femenino"><div contenteditable>'+lines[i][2]+'</div></td><td width="93" class="total"><div contenteditable>'+lines[i][3]+'</div></td><td width="93" class="mes"><div contenteditable>'+lines[i][4]+'</div></td><td width="93" class="ano"><div contenteditable>'+lines[i][5]+'</div></td><td><input type="button" onclick="deleteRow(this);" value="Delete" /></td></tr>')	
}
	
$('#csvFile').val('')

var consultaList = new List('consultas', options);

}


function deleteRow(row)
{
    var i=row.parentNode.parentNode.rowIndex;
    document.getElementById('alldata').deleteRow(i);
}


function addone () {
    $('#alldata').append('<tr><td width="294"><div contenteditable>A</div></td><td width="172"><div contenteditable>A</div></td><td width="172"><div contenteditable>A</div></td><td width="93" ><div contenteditable>A</div></td><td width="93" ><div contenteditable>A</div></td><td width="93" ><div contenteditable>A</div></td><td><input type="button" onclick="deleteRow(this);" value="Delete" /></td></tr>')
}


function tableToJson(table) {   
var data = [];
    
    // first row needs to be headers
    var headers = [];
    for (var i=0; i<table.rows[0].cells.length; i++) {
        headers[i] = table.rows[0].cells[i].innerHTML.toLowerCase().replace(/ /gi,'');
    }

    // go through cells
    for (var i=1; i<table.rows.length; i++) {

        var tableRow = table.rows[i];
        var rowData = {};

        for (var j=0; j<tableRow.cells.length; j++) {

            var cut = (tableRow.cells[j].textContent).replace('</div>', '');
	    cut= cut.replace('<div contenteditable=""> ', '');
            rowData[ headers[j] ] = cut;
        }
	data.push(rowData) 
    }

    $.ajax({
      url:"/management/",
      type:"POST",
      contentType: 'application/json',
      data: JSON.stringify(data),
      dataType: 'text',	
      success: function(res){
 	console.log('its saved')
},
    });	

   
}
