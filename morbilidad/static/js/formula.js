$(document).ready(function () {
    $(document).on('click', '#ecuaciones .mas', function () {
        var row = $(this).closest('tr');
       	
    });

    $(document).on('click', '#ecuaciones .menos', function () {
        var row = $(this).closest('tr');
       	
    });

$(document).on('click', '#ecuaciones .por', function () {
        var row = $(this).closest('tr');
	console.log(row)
       	row.find('td').each(function() {
	if(this.id === "ecua") {
	$(this).val($(this).val() + 'hello')	
	}
});
    });

$(document).on('click', '#ecuaciones .entre', function () {
      	$(this).closest('tr')
	$("td.ecua").append('hello');
    });

$(document).on('click', '#ecuaciones .elevado', function () {
        var row = $(this).closest('tr');
       	
    });

$(document).on('click', '#ecuaciones .variable', function () {
        var row = $(this).closest('tr');
       	
    });	

$(document).on('click', '#ecuaciones .constante', function () {
        var row = $(this).closest('tr');
       	
    });		

   

   });
