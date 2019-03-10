// The base JS which holds all the validation and special "handler" type JS events
// Should also hold all the fancy UI/UX magic
// !!!! TRY TO USE JQUERY, VANILLA JS SHOULD ONLY BE USED FOR THE SIMPLEST OF OPERATIONS

function FocusOnFirstTextInput()
{
    var text_inputs = $("form#form-id-1 :input[type='text']");
    text_inputs[0].focus();
}

function ClearAllTextInput()
{
    $("form#form-id-1 :input[type='text']").each(function(){
        var input = $(this);
        input.val('');
    });
}