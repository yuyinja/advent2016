use strict;
use warnings;


my $COUNT = 0;

sub check_data
{
    my (%data) = @_;
    my $byr = int($data{"byr"});
    unless ($byr >= 1920 && $byr <= 2002)
    {
        return 0;
    }
    my $iyr = $data{"iyr"};
    unless ($iyr >= 2010 && $iyr <= 2020)
    {
        return 0;
    }
    my $eyr = $data{"eyr"};
    unless ($eyr >= 2020 && $eyr <= 2030)
    {
        return 0;
    }
    my $hgt = $data{"hgt"};
    my $hgtsuffix = (substr $hgt, -2);
    my $hgtnum = (substr $hgt, 0, -2);
    if ($hgtsuffix eq "cm")
    {
        unless ($hgtnum >= 150 && $hgtnum <=193)
        {
            return 0;
        }
    }
    elsif ($hgtsuffix eq "in")
    {
        unless ($hgtnum >= 59 && $hgtnum <=76)
        {
            return 0;
        }
    }
    else
    {
        return 0;
    }
    my $hcl = $data{"hcl"};
    my $hclchars = length $hcl;
    my $hclprefix = (substr $hcl, 0, 1);
    unless ($hclprefix eq '#' && $hclchars == 7)
    {
        return 0;
    }
    else
    {
        # check if each char is between 0-9 or a-f
        for my $i (2 .. length $hcl) 
        {
            my $char = substr($hcl, $i-1, 1);
            unless ($char =~ /^\d/ || $char =~ /[a-f]/)
            {
                return 0;
            }
        }
    }
    my $ecl = $data{"ecl"};
    my %eyecolors = ("amb"=>1, "blu"=>1, "brn"=>1, "gry"=>1, "grn"=>1, "hzl"=>1, "oth"=>1);
    unless ($eyecolors{$ecl})
    {
        return 0;
    } 
    my $pid = $data{"pid"};
    my $pidchars = length $pid;
    unless ($pidchars == 9)
    {
        return 0;
    } 
    return 1;
}
sub check_keys
{
    my (%data) = @_;
    my @keys = keys %data;
    my $numkey = @keys;
    # foreach (@keys) {
    #     print "$_ ";
    # }
    if ($numkey == 8)
    {
        $COUNT += check_data(%data);
    }
    elsif ($numkey == 7)
    {
        unless(exists($data{"cid"}))
        {
            $COUNT += check_data(%data);
        }
    }
    return 0;
}

my $filename = 'input.txt';
if (open(my $fh, '<:encoding(UTF-8)', $filename)) {
    my %data = ();
    while (my $row = <$fh>) {
        chomp $row;
        my $rowlength = length $row;
        my %pairs = split /[: ]/, $row;
        @data{ keys %pairs } = values %pairs;
        if ($rowlength == 0)
        {
            check_keys(%data);
            %data = ();
        }
    }
    check_keys(%data);
    print("Final Count:  ", $COUNT);
    close $fh;
  
} else {
  warn "Could not open '$filename' $!";
}

