const URL = 'http://127.0.0.1:5000/'
// const URL = 'http://atorresgolf.pythonanywhere.com/'
// const tabla_inmuebles = document.getElementById('tabla_inmuebles');

fetch(URL + 'inmuebles')
    .then(function(response){
        if(response.ok){
            return response.json();
        }else{
            throw new Error('Error al obtener inmuebles!')
        }
    })

    .then (function(data){
        let tabla_inmuebles = document.getElementById('tablaInmuebles');

        for(let inmueble of data){
            let fila = document.createElement('tr');

            fila.innerHTML = '<td>' + inmueble.id_inmueble + '</td>' +
                        '<td>' + inmueble.direccion + '</td>' +
                        '<td align="right">' + inmueble.localidad + '</td>' +
                        '<td align="right">' + inmueble.provincia + '</td>' +  '<td>' + inmueble.moneda + '</td>' +  '<td>' + inmueble.precio + '</td>' +   '<td>' + inmueble.tipo_inmueble + '</td>' +  '<td>' + inmueble.estado + '</td>' +'<td>' + inmueble.descripcion + '</td>';

                        tabla_inmuebles.append(fila);
        }
    })

    .catch(function(error){
        alert('Error al obtener inmuebles');
    });