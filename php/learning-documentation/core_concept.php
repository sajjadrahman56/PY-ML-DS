<?php

    # this is single line comment 

    echo " We can use '/' or '#' for single line comment";
    // this is also a single line comment 

?>

<?php
 echo "<br><br><br>";

 $x = 10; // global scope 
$y = 100;
 function test_variable()
 {
    $y = 10;
    $x = $y + 5;
    echo " now x inside value add + y = 10 now value = $x";
 }
 test_variable();

 echo "<br><br> ";
 echo "outside value of the x  = $x";

?>

<?php
echo "<br><br><br>";

$x = 10; // global scope 
$y = 100;
 function test_variable2()
 {
    global $x , $y;
    $x = $y * $y;
    $y = $x * $x;
    echo " now x , y inside value x = $x  and y = $y";
 }
 test_variable2();

 echo "<br><br> ";
 echo " now x , y outside value x = $x  and y = $y";

 // global key word use inside the fucntion as the value is update 

?>


<?php
// echo "<br><br><br>";
// print('this is not what we think'.'ok boss '.'<br>');
// // if i not put dot (.) the print can not work 
// echo 'this is not what we think','ok boss ';
?>
<?php
echo "<br><br><br>";
 echo 'now use of the var_dump() to know the data type';
 $x22 = 90909.0999;
 echo '<br>';
 var_dump($x22);
?>

<?php

echo "<br><br>";
$cars = array('abir','sakib','shuvo vai','hasan ali');
echo  $cars[0];
echo '<br><br>';

var_dump($cars);

?>

<?php

echo "<br><br>";
echo "********************* String Operation *********<br><br>";

echo "<br>------ Strlen()------sajjad rahman ----<br>";
echo strlen('sajjad rahman');
echo '<br>';

echo '------ str_word_count()---sajjad rahman-----<br>';
echo str_word_count("sajjad rahamn");
echo "<br>";

echo '------ strrev()---sajjad rahman-----<br>';
echo strrev("sajjad rahamn");
echo "<br>";

echo '------ strpos()------ham-----<br>';
echo strpos("sajjad rahamn","ham");
echo "<br>";

echo '------ str_replace()------rahham -> hussain ----<br>';
echo str_replace("rahman","hussain","sajjad rahman");
echo "<br>";

?>

<?php
echo "<br><br>";
echo "********************* NUMBER OPERATION*********<br><br>";

$data = 10.2;
$num2 = 5;

$num3 = $num2 * $data;

echo " num 3 = $num3";
var_dump($num3);

echo "<br>";
echo "********************* NUMBER Cast *********<br><br>";
$data2 = 4568.890;
$int_cast = (int)$data2;

echo "now int cast of 4568.890  == $int_cast <br><br>";

 
$data3 = 4568;
$float_cast = (float)$data3;

echo "now int cast of 4568.890  === $float_cast <br><br>";
?>

<?php

echo "<br><br>";
echo "********************* PHP Constants  *********<br><br>";

echo " define (name , value , case_sensitive) <br><br>";
define("sajjad","a student of universe",false);

echo sajjad;

echo "<br> ";

echo "********************* define array  ********* <br>";

define("cars",["ab","cd","ef","gh"]);

echo cars[1];

?>