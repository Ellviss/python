<html lang="en" class="h-100">
  <head>
    <meta charset="utf-8">
    <title>MyApp · Bootstrap</title>
    <!-- Bootstrap core CSS -->
    <link href="https://getbootstrap.com/docs/4.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">

    <style>
      .bd-placeholder-img {
        font-size: 1.125rem;
        text-anchor: middle;
        -webkit-user-select: none;
        -moz-user-select: none;
        -ms-user-select: none;
        user-select: none;
      }

      @media (min-width: 768px) {
        .bd-placeholder-img-lg {
          font-size: 3.5rem;
        }
      }
    </style>
    <!-- Custom styles for this template -->
    <link href="https://getbootstrap.com/docs/4.3/examples/sticky-footer/sticky-footer.css" rel="stylesheet">
  </head>
  <body class="d-flex flex-column h-100">
    <?php
    include('work/logic.php');
    include('header.php');
    ?>
    <!-- Begin page content -->
<main role="main" class="flex-shrink-0">
  <div class="container">
    <p class="lead"> NOW: 
    <?php
    $today = date("d. M . Y");
    echo $today;
    ?>
    </p>

      <!-- Begin table with data-->
    <table class="table table-hover">
        <thead class="thead-light">
        <tr>
          <th colspan="4" scope="col">Budget table on current mounth  </th>
          <th> <button type="button" class="btn btn-success">Add</button></th>        
        </tr>
        <tr>
            <th scope="col">#</th>
            <th scope="col">Date</th>
            <th scope="col">Sum</th>
            <th scope="col">Description</th>
            <th scope="col">Actions</th>
        </tr>
        </thead>
        <tbody>
          <?php show_all(); ?>
        </tbody>
    </table>
  </div>
</main>

<footer class="footer mt-auto py-3">
    <?php
    include('footer.php');
    ?>
</footer>
</body>
</html>
