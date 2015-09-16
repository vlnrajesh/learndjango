

$(document).ready(function(){
    $("#id_cmd_aliases").select2();
});


function cloneMore(selector, type) {
    
    //var newElement = $().clone(true);
    var Element = $("#" + selector).children("ul").last();
    if (Element.size() <= 0 ) {
        return; // No element to clone.
    }
    
    var newElement = Element.clone(true);
    
    var total = $('#id_' + type + '-TOTAL_FORMS').val();
    total++;
    
    newElement.find(':input').each(function() {
        var name = $(this).attr('name').replace('-' + (total-1) + '-','-' + total + '-');
        var id = 'id_' + name;
        $(this).attr({'name': name, 'id': id}).val('').removeAttr('checked');
    });
    
    newElement.find('label').each(function() {
        var newFor = $(this).attr('for').replace('-' + (total-1) + '-','-' + total + '-');
        $(this).attr('for', newFor);
    });
    
    
    $('#id_' + type + '-TOTAL_FORMS').val(total);
    
    $("#" + selector).children("ul").after(newElement)
    
    //$(selector).after(newElement);
}