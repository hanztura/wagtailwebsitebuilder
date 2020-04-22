from django.contrib.staticfiles.templatetags.staticfiles import static
from django.forms import widgets, Media, CharField
from django.utils.functional import cached_property
from django.utils.safestring import mark_safe

from pygments import highlight
from pygments.lexers import get_lexer_by_name
from pygments.formatters import get_formatter_by_name
from wagtail.core import blocks
from wagtail.utils.widgets import WidgetWithScript


class CodeTextWidget(WidgetWithScript, widgets.Textarea):
    def render_js_init(self, id_, name, value):
        jsinit = """
            if (window.ACEInstances == null) {{
                window.ACEInstances = {{}};
            }}
            // get the information used to create ace editor for each block
            var code_value_id = "{id!s}"
            var mode_value_id = code_value_id.replace("code", "language");
            var code = document.getElementById(code_value_id);
            var mode = document.getElementById(mode_value_id).value;
            // mode_map is defined in aes_utils.jp
            mode = mode_map[mode];
            var code_panel = document.createElement("div");
            code.parentElement.appendChild(code_panel);
            code.style.display = "none";

            // create ace editor
            var _editor = ace.edit(code_panel);

            // setup editor
            _editor.$blockScrolling = Infinity;
            _editor.container.style.height = "300px"
            _editor.container.style.weight = "100%"
            _editor.resize()
            _editor.setTheme("ace/theme/chrome");
            _editor.setShowPrintMargin(false);
            _editor.setFontSize(13);

            // setup editor session
            _editor.getSession().setUseWorker(false);
            _editor.getSession().setUseSoftTabs(true);
            _editor.getSession().setValue(code.value);
            _editor.getSession().setMode("ace/mode/" + mode);

            // added event listener to update code textarea
            // pass session into the function to bind the corresponding
            // textarea.
            _editor.getSession().on("change", function(e, _session) {{
                var code = document.getElementById("{id!s}");
                code.value = _session.getValue();
            }});

            window.ACEInstances[code_value_id] = _editor;
        """
        return jsinit.format(id=id_)

    @property
    def media(self):
        js = [
            static('vendor/ace/ace.js'),
            static('vendor/ace/utils.js'),
        ]
        return Media(js=js)


class CodeChoiceBlock(blocks.ChoiceBlock):
    def __init__(
            self, choices=None, default=None,
            required=True, help_text=None, **kwargs):
        super(CodeChoiceBlock, self).__init__(choices=choices,
                                              default=default,
                                              required=required,
                                              help_text=help_text,
                                              **kwargs)
        self.field.widget.attrs.update({'onchange': 'update_code_mode(this)'})


LANGUAGES = (
    ('python3', 'Python 3'),
    ('bash', 'Bash/Shell'),
    ('javascript', 'Javascript'),
    ('css', "CSS"),
    ('html', "HTML"),
)


class CodeTextBlock(blocks.TextBlock):
    @cached_property
    def field(self):
        field_kwargs = {
            'widget': CodeTextWidget(),
        }
        field_kwargs.update(self.field_options)
        return CharField(**field_kwargs)


class CodeBlock(blocks.StructBlock):
    language = CodeChoiceBlock(
        choices=LANGUAGES, blank=False, null=False, default='python')
    caption = blocks.CharBlock(required=False, blank=True, nullable=True)
    code = CodeTextBlock()

    def render(self, value, *args, **kwargs):
            src = value['code'].strip('\n')
            caption = value['caption'].strip()
            lang = value['language']
            lexer = get_lexer_by_name(lang)
            formatter = get_formatter_by_name(
                'html',
                linenos=None,
                cssclass='codehilite',
                style='github',
                noclasses=False,
            )
            render_content = highlight(src, lexer, formatter)
            if caption:
                caption_content = '<div class="code-caption">{}</div>\n'
                caption_content = caption_content.format(caption)
                render_content = caption_content + render_content
            return mark_safe(render_content)

    class Meta:
        icon = "code"
