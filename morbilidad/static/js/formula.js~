$(document).ready(function () {
    $(document).on('click', '#ecuaciones .add', function () {
        var row = $(this).closest('tr');
	console.log(row)
        var clone = row.clone();
        var tr = clone.closest('tr');
        $("td.ecua", tr).text("");
	$("td.asig", tr).text(""); 
        $(this).closest('tr').after(clone);
        var $span = $("#ecuaciones tr");
    });

    $(document).on('click', '#ecuaciones .delete', function () {
        if ($('#ecuaciones .add').length > 0) {
            $(this).closest('tr').remove();
        }

    });

    $("#asig").keydown(function (e) {
        // backspace, delete, tab, escape, enter
        if ($.inArray(e.keyCode, [46, 8, 9, 27, 13]) !== -1 ||
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

function guardar(table) {   
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
            rowData[ headers[j] ] = cut;
        }
	data.push(rowData) 
    }

    $.ajax({
      url:"/editeq/",
      type:"POST",
      contentType: 'application/json', 
      data: JSON.stringify(data),
      dataType: 'text',	
      success: function(res){
 	console.log('its saved')
},
    });	

   
}
