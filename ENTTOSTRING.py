# !/usr/bin/python
# -*- coding: utf-8 -*-

__author__ = 'sjohnson'

import sys
import os
import shutil
import re
import codecs


def sub_array():
    sub_regex = [
        [re.compile("&(#024);", re.MULTILINE), "[\g<1>]"],
        [re.compile("&(#032);", re.MULTILINE), "[\g<1>]"],
        [re.compile("&(all);", re.MULTILINE), "[\g<1>]"],
        [re.compile("&amp;", re.MULTILINE), u"&"],
        [re.compile("&apos;", re.MULTILINE), u"'"],
        [re.compile("&(ast);", re.MULTILINE), "[\g<1>]"],
        [re.compile("&(atilde);", re.MULTILINE), "[\g<1>]"],
        [re.compile("&(ballot);", re.MULTILINE), "[\g<1>]"],
        [re.compile("&(bdlarr);", re.MULTILINE), "[\g<1>]"],
        [re.compile("&(bdrarr);", re.MULTILINE), "[\g<1>]"],
        [re.compile("&(bdsol);", re.MULTILINE), "[\g<1>]"],
        [re.compile("&bull;", re.MULTILINE), u"<bullet>"],
        [re.compile("&(cent);", re.MULTILINE), "[\g<1>]"],
        [re.compile("&chyph;", re.MULTILINE), u" "],
        [re.compile("&commat;", re.MULTILINE), u"@"],
        [re.compile("&copy;", re.MULTILINE), u"(copyright)"],
        [re.compile("&(deg);", re.MULTILINE), "[\g<1>]"],
        [re.compile("&divide;", re.MULTILINE), u"/"],
        [re.compile("&dollar;", re.MULTILINE), u"$"],
        [re.compile("&(dprime);", re.MULTILINE), "[\g<1>]"],
        [re.compile("&(eacute);", re.MULTILINE), "[\g<1>]"],
        [re.compile("&emsp;", re.MULTILINE), u' '],
        [re.compile("&ensp;", re.MULTILINE), u' '],
        [re.compile("&equal;", re.MULTILINE), u'='],
        [re.compile("&equals;", re.MULTILINE), u'='],
        [re.compile("&fnl;", re.MULTILINE), u' '],
        [re.compile("&(foot);", re.MULTILINE), "[\g<1>]"],
        [re.compile("&(frac1s2);", re.MULTILINE), "[\g<1>]"],
        [re.compile("&fxsp0;", re.MULTILINE), u' '],
        [re.compile("&ge;", re.MULTILINE), u'>='],
        [re.compile("&gt;", re.MULTILINE), u'>'],
        [re.compile("&(hairsp);", re.MULTILINE), "[\g<1>]"],
        [re.compile("&(half);", re.MULTILINE), "[\g<1>]"],
        [re.compile("&(iexcl);", re.MULTILINE), "[\g<1>]"],
        [re.compile("&inch;", re.MULTILINE), u'"'],
        [re.compile("&(infin);", re.MULTILINE), "[\g<1>]"],
        [re.compile("&(iquest);", re.MULTILINE), "[\g<1>]"],
        [re.compile("&lcub;", re.MULTILINE), u'{'],
        [re.compile("&ldquo;", re.MULTILINE), u'``'],
        [re.compile("&le;", re.MULTILINE), u'<='],
        [re.compile("&llmdash;", re.MULTILINE), u'_'],
        [re.compile("&lowbar;", re.MULTILINE), u'_'],
        [re.compile("&lowbarm;", re.MULTILINE), u'_'],
        [re.compile("&(lparb);", re.MULTILINE), "[\g<1>]"],
        [re.compile("&(lsqb);", re.MULTILINE), "[\g<1>]"],
        [re.compile("&lsquo;", re.MULTILINE), u'`'],
        [re.compile("&lt;", re.MULTILINE), u'<'],
        [re.compile("&mdash;", re.MULTILINE), u'_'],
        [re.compile("&mgr;", re.MULTILINE), u'micro'],
        [re.compile("&(micro);", re.MULTILINE), "[\g<1>]"],
        [re.compile("&(middot);", re.MULTILINE), "[\g<1>]"],
        [re.compile("&minus;", re.MULTILINE), u'-'],
        [re.compile("&(mu);", re.MULTILINE), "[\g<1>]"],
        [re.compile("&ndash;", re.MULTILINE), u"\u2013"],
        [re.compile("&(ntilde);", re.MULTILINE), "[\g<1>]"],
        [re.compile("&num;", re.MULTILINE), u'#'],
        [re.compile("&numsign;", re.MULTILINE), u'#'],
        [re.compile("&(ohm);", re.MULTILINE), "[\g<1>]"],
        [re.compile("&para;", re.MULTILINE), u"\u0014"],
        [re.compile("&(Pi);", re.MULTILINE), "[\g<1>]"],
        [re.compile("&plus;", re.MULTILINE), u'+'],
        [re.compile("&plusmn;", re.MULTILINE), u'<plus-minus>'],
        [re.compile("&Prime;", re.MULTILINE), u"''"],
        [re.compile("&prime;", re.MULTILINE), u"'"],
        [re.compile("&(Primes);", re.MULTILINE), "[\g<1>]"],
        [re.compile("&qdrt;", re.MULTILINE), u"\u0003"],
        [re.compile("&(radic);", re.MULTILINE), "[\g<1>]"],
        [re.compile("&rcub;", re.MULTILINE), u"}"],
        [re.compile("&rdquo;", re.MULTILINE), u"''"],
        [re.compile("&(reg);", re.MULTILINE), "[\g<1>]"],
        [re.compile("&(rparb);", re.MULTILINE), "[\g<1>]"],
        [re.compile("&(rsqb);", re.MULTILINE), "[\g<1>]"],
        [re.compile("&rsquo;", re.MULTILINE), u"'"],
        [re.compile("&sbull;", re.MULTILINE), u"<bullet>"],
        [re.compile("&sect;", re.MULTILINE), u"\u00A7"],
        [re.compile("&(Sigma);", re.MULTILINE), "[\g<1>]"],
        [re.compile("&(sigma);", re.MULTILINE), "[\g<1>]"],
        [re.compile("&sim;", re.MULTILINE), u"~"],
        [re.compile("&thnsp;", re.MULTILINE), u' '],
        [re.compile("&tilde;", re.MULTILINE), u"~"],
        [re.compile("&times;", re.MULTILINE), u"x"],
        [re.compile("&(uuml);", re.MULTILINE), "[\g<1>]"],
        [re.compile("&#224;", re.MULTILINE), u"a"],
        [re.compile("&#xE0;", re.MULTILINE), u"a"],
        [re.compile("&#x0E0;", re.MULTILINE), u"a"],
        [re.compile("&#x00E0;", re.MULTILINE), u"a"],
        [re.compile("&#225;", re.MULTILINE), u"a"],
        [re.compile("&#xE1;", re.MULTILINE), u"a"],
        [re.compile("&#x00E1;", re.MULTILINE), u"a"],
        [re.compile("&#232;", re.MULTILINE), u"e"],
        [re.compile("&#xE8;", re.MULTILINE), u"e"],
        [re.compile("&#x0E8;", re.MULTILINE), u"e"],
        [re.compile("&#x00E8;", re.MULTILINE), u"e"],
        [re.compile("&#233;", re.MULTILINE), u"e"],
        [re.compile("&#xE9;", re.MULTILINE), u"e"],
        [re.compile("&#x0E9;", re.MULTILINE), u"e"],
        [re.compile("&#x00E9;", re.MULTILINE), u"e"],
        [re.compile("&#241;", re.MULTILINE), u"n"],
        [re.compile("&#xF1;", re.MULTILINE), u"n"],
        [re.compile("&#x0F1;", re.MULTILINE), u"n"],
        [re.compile("&#x00F1;", re.MULTILINE), u"n"],
        [re.compile("&#X201C;", re.MULTILINE), u"``"],
        [re.compile("&#X201D;", re.MULTILINE), u"''"],
    ]
    return sub_regex


def replace(filename, regexes, do_all):
    """
    Replaces occurences of patterns in a dict with corresponding string in a given file

    @type filename: str
    @type regexes: list
    @param filename: filename where replacements should take place
    @param regexes: list of compiled replacement patterns [search pattern, replacement string]
    """
    with codecs.open(filename, mode='r', encoding='utf-8') as content_file:
        file_string = content_file.read()



    # Use RE package to allow for replacement (also allowing for (multiline) REGEX)
    for pattern in regexes:
        try:
            file_string = pattern[0].sub(pattern[1], file_string)
        except Exception as e:
            sys.exit(e.__str__())

    if do_all:
        try:
            file_string = re.compile("&([^\s]*?);", re.MULTILINE).sub("[\g<1>]", file_string)
        except Exception as e:
            sys.exit(e.__str__())
    else:
        try:
            file_string = re.compile("&[^\s]*?;", re.MULTILINE).sub("", file_string)
        except Exception as e:
            sys.exit(e.__str__())

    # Write contents to file.
    # Using mode 'w' truncates the file.
    with codecs.open(filename, mode='w', encoding='utf-8') as file_handle:
        file_handle.write(file_string)
    return


def copy_file(in_file, out_file):
    try:
        dest_file = open(out_file, 'wb')
    except IOError:
        sys.exit('Error: Unable to create output file!')
    try:
        src_file = open(in_file, 'rb')
    except IOError:
        sys.exit('Error: Input file does not appear to exist!')
    shutil.copyfileobj(src_file, dest_file)
    dest_file.close()
    return


def replace_entities(in_file, all_flag):
    if os.path.isfile(in_file) and all_flag:
        replace(in_file, sub_array(), all_flag),
    else:
        replace(in_file, sub_array(), all_flag),
    return


if __name__ == "__main__":
    input_file = ''
    output_file = ''

    if len(sys.argv) < 3 or len(sys.argv) > 4:
        sys.exit('Please use format:  ENTTOSTRING.exe <input_file> <output_file> [/all]')
    else:
        if os.path.isfile(sys.argv[1]):
            input_file = sys.argv[1]
        else:
            sys.exit('Input file is not located!!!')

        output_file = sys.argv[2]

        copy_file(input_file, output_file)
        if len(sys.argv) == 3 and '/all' not in sys.argv:
            replace_entities(output_file, False)
        elif len(sys.argv) == 4 and '/all' in sys.argv:
            replace_entities(output_file, True)

        print "File successfully processed and located here: ", output_file
