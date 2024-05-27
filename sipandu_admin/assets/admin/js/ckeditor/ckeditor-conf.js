CKEDITOR.replace( 'message' );
CKEDITOR.config.allowedContent = true;
CKEDITOR.config.removeFormatAttributes = '';
CKEDITOR.config.height = '18.5em';
CKEDITOR.config.width = '100%';
CKEDITOR.config.toolbarGroups = [
    { name: 'document', groups: [ 'mode', 'document', 'doctools' ] },
    { name: 'basicstyles', groups: [ 'basicstyles', 'cleanup' ] },
    { name: 'paragraph', groups: [ 'list', 'indent', 'blocks', 'align', 'bidi', 'paragraph' ] },
    { name: 'clipboard', groups: [ 'clipboard', 'undo' ] },
    { name: 'forms', groups: [ 'forms' ] },
    { name: 'editing', groups: [ 'find', 'selection', 'spellchecker', 'editing' ] },
    { name: 'links', groups: [ 'links' ] },
    { name: 'insert', groups: [ 'insert' ] },
    { name: 'styles', groups: [ 'styles' ] },
    { name: 'colors', groups: [ 'colors' ] },
    { name: 'tools', groups: [ 'tools' ] },
    { name: 'others', groups: [ 'others' ] },
    { name: 'about', groups: [ 'about' ] }
];
CKEDITOR.config.removeButtons = 'Source,Save,NewPage,ExportPdf,Preview,Print,Templates,CreateDiv,Language,Form,Checkbox,Radio,TextField,Textarea,Select,Button,ImageButton,HiddenField,Find,Replace,SelectAll,PageBreak,Iframe,Anchor';

// CKEDITOR.config.removeButtons = 'Source,Save,NewPage,ExportPdf,Preview,Print,Templates,Cut,Copy,Paste,PasteText,PasteFromWord,Find,
// Replace,SelectAll,Form,Checkbox,Radio,TextField,CopyFormatting,RemoveFormat,Italic,Underline,Strike,Subscript,Superscript,Textarea,
// Select,Button,ImageButton,HiddenField,Blockquote,CreateDiv,Outdent,Indent,JustifyLeft,JustifyCenter,JustifyRight,JustifyBlock,Language,Link,
// Image,Flash,Unlink,Anchor,Table,HorizontalRule,Smiley,SpecialChar,PageBreak,Iframe,FontSize,Font,Format,Styles,TextColor,
// ShowBlocks,Maximize,About,BGColor';