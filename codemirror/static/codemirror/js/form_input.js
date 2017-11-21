// assuming this is used in a form
// when submit is clicked, pull the text from the textbox and add it to the form's data
// the variable code_editor is from widgets.py where we create the codemirror instance

window.onload = function() {

    function update_textarea() {
        code_editor.save();
    }

    code_editor.on('change', update_textarea);
};
