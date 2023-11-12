#!"C:/xampp/perl/bin/perl.exe"
use strict;
use warnings;
use CGI;
use Text::CSV;

my $cgi = CGI->new;

my $nombreUni    = $cgi->param('nombreUniversidad');
my $periodoLic   = $cgi->param('periodoLicenciamiento');
my $depLocal     = $cgi->param('departamentoLocal');
my $denoProg     = $cgi->param('denominacionPrograma');

my $archivo = 'C:\xampp\htdocs\csv.csv';
open my $fh, '<', $archivo;

my $csv = Text::CSV->new({ binary => 1, sep_char => '|' });

my $tableKey = "";
if (my $fila = $csv->getline($fh)) {
    for my $valor (@$fila) {
        $tableKey .= "<th>$valor</th>\n";
    }
}

my $tableValues = "";
my $v = "";

while (my $fila = $csv->getline($fh)) {
    $v .= $fila->[16];
    if (($fila->[16] eq $denoProg)) {
        $tableValues .= "<tr>";
        for my $valor (@$fila) {
            $tableValues .= "<td>$valor</td>\n";
        }
        $tableValues .= "</tr>";
    }
}


close $fh;

print $cgi->header('text/html');
print <<HTML;

<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Resultados de la búsqueda</title>
</head>
<body>
    <h1>Resultados de la búsqueda</h1>
    <table border="1">
        <tr>$tableKey</tr>
        $tableValues
    </table>
</body>
</html>
HTML