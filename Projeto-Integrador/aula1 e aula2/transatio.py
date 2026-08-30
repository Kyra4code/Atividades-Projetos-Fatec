import os;
import gettext;

def translation():
    os.system(command="msgfmt lang/pt_BR/LC_MESSAGES/translation.po -o lang/pt_BR/LC_MESSAGES/translation.mo && msgfmt lang/en/LC_MESSAGES/translation.po -o lang/en/LC_MESSAGES/translation.mo")

    gettext.bindtextdomain(domain='translation', localedir='./lang')
    gettext.textdomain('translation');
    x = gettext.gettext

    translation = gettext.translation('translation', localedir='./lang', languages=['pt_BR'])
    translation.install()

    return x
