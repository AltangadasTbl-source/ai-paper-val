use strict;
use warnings;
while (<>) {
    next unless /RapidOCR - INFO: \[\[\[\[/;
    while (/(['"])((?:\\.|(?!\1).)*)\1, [0-9.e+\-]+\]/g) {
        my $ocr_line = $2;
        $ocr_line =~ s/\\'/'/g;
        $ocr_line =~ s/\\"/"/g;
        print "$ocr_line\n";
    }
}
