// The base JS which holds all the validation and special "handler" type JS events
// Should also hold all the fancy UI/UX magic
// !!!! TRY TO USE JQUERY, VANILLA JS SHOULD ONLY BE USED FOR THE SIMPLEST OF OPERATIONS

function IsEmpty(p_text)
{
    var re;
    // at least one non-space char in string
    re = new RegExp(/\S+/);
    if (!p_text || !re.test(p_text)) {
        return true;
    }
    return false;
}

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

function FormPreSubmitConfirmation(p_button_name, p_kwargs)
{
    l_title        = "Perform the action?";
    l_text         = "Are you sure you would like to carry on with this process as it is non-reversible?";
    l_type         = "warning";
    l_success_title= "Completed.";
    l_success_text = "The process is now completed.";

    if (p_kwargs) {
        // we must specify what action triggers this, even if it's a single submit button form
        if (IsEmpty(p_kwargs['action'])) {
            return false;
        }
        else {
            // just go ahead and submit if the button clicked is not the event trigger
            if ( !(p_kwargs['action'] === p_button_name) ) {
                return true;
            }
        }

        if (!IsEmpty(p_kwargs['title'])) {
            l_title        = p_kwargs['title'];
        }
        if (!IsEmpty(p_kwargs['text'])) {
            l_title        = p_kwargs['text'];
        }
        if (!IsEmpty(p_kwargs['success_title'])) {
            l_success_title= p_kwargs['success_title'];
        }
        if (!IsEmpty(p_kwargs['success_text'])) {
            l_success_text = p_kwargs['success_text'];
        }

        swal(
            {
              title      : l_title,
              text       : l_text,
              icon       : l_type,
              buttons    : {
                cancel   : true,
                confirm  : {
                    text : "Confirm",
                    value: "confirm",
                },
              }
            },
        ).then(
            (value) => {
                switch (value) {
                    case "confirm":
                        // swal(l_success_title, l_success_text, "success").then(
                            // function()
                            // {
                            // $("#form-action").val(p_button_name);
                            SetFormAction($('input[name="'+p_button_name+'"]').closest("form"), {'form-action' : p_button_name});
                            $('input[name="'+p_button_name+'"]').closest("form").submit();
                            // }
                        // );
                        break;
                    default:
                        return false;
                }
            }
        );
    }
    return false;
}

function SetFormActionThenSubmit(p_kwargs)
{
    // the action to be performed
    if (IsEmpty(p_kwargs['form-action'])) {
        return false;
    }
    l_form_action = p_kwargs['form-action'];

    // the id of the form to be submitted
    l_form_name = 'form-id-1';
    if (!IsEmpty(p_kwargs['form-name'])) {
        l_form_name = p_kwargs['form-name'];
    }

    // the hidden input field which will hold the action keyword
    l_action_field = 'form-action';
    if (!IsEmpty(p_kwargs['action-field'])) {
        l_action_field = p_kwargs['action-field'];
    }

    $("#"+l_action_field).val(l_form_action);
    $("#"+l_form_name).submit();
}

function SetFormAction(p_form, p_kwargs)
{
    // the action to be performed
    if (IsEmpty(p_kwargs['form-action'])) {
        return false;
    }
    l_form_action = p_kwargs['form-action'];

    // the id of the form to be submitted
    l_form_name = p_form.id;

    // the hidden input field which will hold the action keyword
    l_action_field = 'form-action';
    if (!IsEmpty(p_kwargs['action-field'])) {
        l_action_field = p_kwargs['action-field'];
    }

    $("#"+l_action_field).val(l_form_action);
    console.log('a'+$("#"+l_action_field).val())
}