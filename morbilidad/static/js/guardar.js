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
        data.push(rowData); 
    }

    $.ajax({
      url:"",
      type:"POST",
      contentType: 'application/json',
      data: JSON.stringify(data),
      dataType: 'text',	
      success: function(res){
 	console.log('its saved')
},
    });	

   
}
