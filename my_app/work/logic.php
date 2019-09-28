<?php

// work with DB
function connect()
{
	$connection = mysqli_connect('localhost', 'root','homecredit', 'buh') or die(mysqli_error());
	return($connection);
}

//work with content

function show_all()
{
	$col_num=1;
	$date_today = date("d.m.Y");
	$query = "SELECT * FROM `notes` ORDER BY `date` DESC ";
    $result = mysqli_query(connect(), $query) or die('Error querying database.');
    while ($row = mysqli_fetch_array($result)){
         $id = $row['id'];
         $text = $row['text_'];
         $cost = $row['cost_'];
         $date = $row['date'];
		 $type = $row['type'];
		 if ($type==1)
    	{		$class = "table-success";	}
    	else
    	{		$class = "table-danger";	}

		echo '<tr class='. $class .'>';   
		echo '<th>' . $col_num++ .'</th>';
		echo '<td >' . $date .'</td>';
		echo '<td>'. $cost .'</td>';
		echo '<td> '. $text .' </td>';
		echo '<td>
				<input class="btn btn-primary" type="button" value="Edit">
                <input class="btn btn-danger"  type="submit" value="Delete">
                <input class="btn btn-info"    type="reset" value="Reset">
		</td>';
		echo '</tr>';
    }  
}

function show_amount()
{
	
}
function show_one()
{

}

function del_one()
{

}

function edit_one()
{

}

function add_one()
{

}
?>