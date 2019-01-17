<?php echo "Fan Control"?>

<FORM action="<?=$_SERVER['PHP_SELF']?>" method = "post">

<input type="submit" name="submitted" value="ON"/>
<input type="submit" name="submitted" value="OFF"/>

</FORM>

<FORM action="<?=$_SERVER['PHP_SELF']?>" method = "post">

<input type="submit" name="submitted" value="LOW"/>
<input type="submit" name="submitted" value="MED"/>
<input type="submit" name="submitted" value="HIGH"/>

</FORM>

<FORM action="<?=$_SERVER['PHP_SELF']?>" method = "post">

<input type="submit" name="submitted" value="EXIT"/>

</FORM>

<?php

	switch($_POST['submitted'])
	{
		case "ON":
		$OFFpython = "^C";
		$cmd = exec($OFFpython);
		$OFFpython = "sudo python /var/www/html/G1.py 1";
		$cmd = exec($OFFpython);
		echo "<pre>$cmd</pre>";
		break;
		
		case "OFF":
		$OFFpython = "^C";
		$cmd = exec($OFFpython);
		$OFFpython = "sudo python /var/www/html/G1.py 0";
		$cmd = exec($OFFpython);
		echo "<pre>$cmd</pre>";
		break;
		
		case "LOW":
		echo "LOW";
		break;
		
		case "MED":
		break;
		
		case "HIGH":
		break;
		
		case "EXIT":
		$OFFpython = "sudo python /var/www/html/G1.py 3";
		$cmd = exec($OFFpython);
		echo "<pre>$cmd</pre>";
		break;
		
				}

?>
