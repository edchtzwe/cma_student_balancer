// The base JS which holds all the validation and special "handler" type JS events
// Should also hold all the fancy UI/UX magic
// !!!! TRY TO USE JQUERY, VANILLA JS SHOULD ONLY BE USED FOR THE SIMPLEST OF OPERATIONS

function FocusOnFirstTextInput()
{
    var text_inputs = $("form#form-id-1 input[type='text']");
    if (text_inputs.length > 0) {
        text_inputs[0].focus();
        return;
    }
    var number_inputs = $("form#form-id-1 input[type='number']");
    if (number_inputs.length > 0) {
        number_inputs[0].focus();
        if ($("#"+number_inputs[0].id).val() == 0) {
            $("#"+number_inputs[0].id).select();
        }
        return;
    }
}

function ClearAllTextInput()
{
    $("form#form-id-1 :input[type='text']").each(function(){
        var input = $(this);
        input.val('');
    });
}

function NumericalOnly(p_field_id)
{
    var re;
    // at least one non-space char in string
    re = new RegExp(/\S+/);
    if (!p_field_id || !re.test(p_field_id)) {
        swal('Oops!', 'No validation parameters were passed, please contact your system adminstrator to resolve this issue.', 'error');
        return false;
    }
    re = new RegExp(/^(\d+\.?\d*)$/);
    field_value = $("#" + p_field_id).val();
    console.log("field_value : " + field_value);
    if (!re.test(field_value)) {
        swal('Oops!', 'The value entered is not numerical.', 'error');
        return false;
    }
    return true;
}

function SubmissionValidation(p_function_array)
{
    if (!p_function_array || !p_function_array.length) {
        return true;
    }
    $.each(p_function_array, function(index, value) {
        var a;
    });
}