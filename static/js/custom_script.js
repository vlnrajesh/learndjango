

$(document).ready(function(){
    $("#id_cmd_aliases").select2();
});


function cloneMore(selector, type) {
    
    var idRegx = /(\w+-)\d+(-\w+)/;
    
    //var newElement = $().clone(true);
    var Element = $("#" + selector).children("ul").last();
    if (Element.size() <= 0 ) {
        return; // No element to clone.
    }
    
    var newElement = Element.clone(true);
    
    var total = $('#id_' + type + '-TOTAL_FORMS').val();    
    total++;
    
    // input change.
    newElement.find(':input').each(function() {
        var name = $(this).attr('name').replace(idRegx, '$1' + (total-1) + '$2');
        var id = 'id_' + name;
        $(this).attr({'name': name, 'id': id}).val('').removeAttr('checked');
    });
    
    newElement.find('label').each(function() {
        var newFor = $(this).attr('for').replace(idRegx, '$1' + (total - 1) + '$2');
        $(this).attr('for', newFor);
    });
    
    newElement.find('div').each(function() {
        if($(this).attr("id") != undefined) {
            var newId = $(this).attr('id').replace(idRegx, '$1' + (total-1) + '$2');
            $(this).attr('id', newId);
        }
    });
    
    newElement.find('p').each(function() {
        if($(this).attr("id") != undefined) {
            var newId = $(this).attr('id').replace(idRegx, '$1' + (total-1) + '$2');
            $(this).attr('id', newId);
        }
    });
    
    newElement.find('textarea').each(function() {
        var newFor = $(this).attr('name').replace(idRegx, '$1' + (total-1) + '$2');
        var id = 'id_' + name;
        $(this).attr({'name': name, 'id': id}).val('');
    });
    
    $('#id_' + type + '-TOTAL_FORMS').val(total);
    
    $("#" + selector).append(newElement);

}

function changeAttrCount(element, attrName) {
    var newAttrVal = element.attr(attrName).replace(idRegx, '$1' + total + '$2');
    var id = 'id_' + newAttrVal;
    $(this).attr({attrName: newAttrVal, 'id': id}).val('').removeAttr('checked');
}