<?php
    function connect()
    {
    $connection = mysqli_connect("localhost", "root", "homecredit", "buh");
    if (!$connection) {
        echo "Ошибка: Невозможно установить соединение с MySQL." . PHP_EOL;
        echo "Код ошибки errno: " . mysqli_connect_errno() . PHP_EOL;
        echo "Текст ошибки error: " . mysqli_connect_error() . PHP_EOL;
        exit;
    }
    return $connection;
    
    }
    $date_today = date("d.m.Y");
    $query = "SELECT * FROM `notes` ORDER BY `date` DESC ";
    $result = mysqli_query(connect(), $query) or die('Error querying database.');
    while ($row = mysqli_fetch_array($result)){
         $id = $row['id'];
         $text = $row['text_'];
         $cost = $row['cost_'];
         $date = $row['date'];
         $type = $row['type'];
         echo $cost;
    }
    printf("Select вернул %d строк.\n", mysqli_num_rows($result));
    mysqli_free_result($result);
    
?>