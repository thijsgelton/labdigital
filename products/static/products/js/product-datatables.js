$(document).ready(function () {
    const table = $('#products').DataTable({
        dom: 'Bfrtip',
        search: {"regex": true},
        serverSide: true,
        ajax: "/api/products/?format=datatables",
        language: {"searchPlaceholder": "Regular expression"},
        columnDefs: [
            {
                render: function (data, type, row) {
                    console.log(row);
                    return '<a href="details/' + row['id'] + '"><img src="' + row ['image'].thumbnail + '"</img></a>';
                },
                targets: 1
            },
            {visible: false, "targets": [0]}
        ],
        buttons: [
            {
                text: 'New product',
                action: function (e, dt, node, config) {
                    window.location = "/new"
                }
            }
        ]
    });
    new $.fn.dataTable.Buttons(table, {
        buttons: [
            'excel',
            'csv',
            'pdf'
        ]
    });
    table.buttons(1, null).container().appendTo(table.table().container());
});