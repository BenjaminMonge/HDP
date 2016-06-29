var options = {
  valueNames: [ 'enfermedad', 'masculino', 'femenino', 'total', 'mes', 'ano',]
};

var consultaList = new List('consultas', options);

$(document).ready(function () {
    $(document).on('click', '#alldata .add', function () {

        var row = $(this).closest('tr');
        var clone = row.clone();
        var tr = clone.closest('tr');
	tr.css('background-color','#FFFFFF');
        $("td.enfermedad", tr).text("");
	$("td.masculino", tr).text(""); 
	$("td.femenino", tr).text(""); 
	$("td.total", tr).text(""); 
	$("td.mes", tr).text(""); 
 	$("td.ano", tr).text(""); 
        $(this).closest('tr').after(clone);
        var $span = $("#alldata tr");
    });

    $(document).on('click', '#alldata .delete', function () {
        if ($('#alldata .add').length > 0) {
            $(this).closest('tr').remove();
        }

    });

    $("#total, #masculino, #femenino, #ano").keydown(function (e) {
        // Allow: backspace, delete, tab, escape, enter and .
        if ($.inArray(e.keyCode, [46, 8, 9, 27, 13, 110, 190]) !== -1 ||
             // Allow: Ctrl+A
            (e.keyCode == 65 && e.ctrlKey === true) ||
             // Allow: Ctrl+C
            (e.keyCode == 67 && e.ctrlKey === true) ||
             // Allow: Ctrl+X
            (e.keyCode == 88 && e.ctrlKey === true) ||
             // Allow: home, end, left, right
            (e.keyCode >= 35 && e.keyCode <= 39)) {
                 // let it happen, don't do anything
                 return;
        }
        // Ensure that it is a number and stop the keypress
        if ((e.shiftKey || (e.keyCode < 48 || e.keyCode > 57)) && (e.keyCode < 96 || e.keyCode > 105)) {
            e.preventDefault();
        }
    });	

});




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

	reader.onload = loadHandler;
	reader.onerror = errorHandler;

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
	for(var i=0; i<lines.length-1; i++) {
	
	    $('#alldata').append('<tr><td width="294" class="enfermedad" type="text" contenteditable="true"> '+lines[i][0]+' </td><td width="172" id="masculino" class="masculino" type="number" contenteditable="true"> '+lines[i][1]+' </td><td width="172" id="femenino" class="femenino" type="number" contenteditable="true"> '+lines[i][2]+' </td><td width="93" id="total" class="total" contenteditable="true"> '+lines[i][3]+' </td><td width="93" class="mes" type="text" contenteditable="true"> '+lines[i][4]+'</td><td width="93" id="ano" class="ano" type="text" contenteditable="true"> '+lines[i][5]+'</td><td><input type="button" class="add" value="Nueva" /></td><td><input type="button" class="delete" value="Borrar" /></td>/tr>')	
}

	
$('#csvFile').val('')

var consultaList = new List('consultas', options);

}

function tableToJson(table) {   
var data = [];
    
    // first row needs to be headers
    var headers = [];
    for (var i=0; i<table.rows[0].cells.length; i++) {
        headers[i] = table.rows[0].cells[i].innerHTML.toLowerCase().replace(/ /gi,'').replace('ñ', 'n');
    }

    // go through cells
    for (var i=1; i<table.rows.length; i++) {

        var tableRow = table.rows[i];
        var rowData = {};

        for (var j=0; j<tableRow.cells.length-2; j++) { 	
            var cut = (tableRow.cells[j].textContent)
	    if(j!==0){
		cut.replace(' ', '')
	    }	
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
