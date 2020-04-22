mode_map = {
    "cpp": "c_cpp",
    "java": "java",
    "python":"python",
    "python3": "python",
    "bash": "sh",
    "javascript": "javascript",
    "css": "css",
    "html": "html",
}
function update_code_mode(obj) {
    var choice_id = obj.id;
    var editor_id = choice_id.replace("language", "code");
    var code_mode = "ace/mode/" + mode_map[obj.value];
    var _editor = window.ACEInstances?window.ACEInstances[editor_id]:null;
    if (_editor) _editor.getSession().setMode(code_mode);
}
