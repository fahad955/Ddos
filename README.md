HEllo Users 


<h1>Lets Jam Any WEBsites </h1>


<h2>installing Proses</h2>


<?php

require __DIR__ . '/vendor/autoload.php';

use Povils\Figlet\Figlet;

// Default font is "big"
$figlet = new Figlet();

//Outputs "Figlet" text using "small" red font in blue background.
$figlet
    ->setFont('small')
    ->setFontColor('red')
    ->setBackgroundColor('blue')
    ->write('Figlet');

//Returns rendered string.
$renderedFiglet = $figlet->render('Another Figlet')

- setFontDir(__DIR_ . '/fonts') // Change default font directory
- setFontStretching(3) // Add spaces between letters
