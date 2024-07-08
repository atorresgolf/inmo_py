const URL = 'http://127.0.0.1:5000/'
// const tabla_inmuebles = document.getElementById('tabla_inmuebles');

fetch(URL + 'inmuebles')
    .then(function(response){
        if(response.ok){
            return response.json();
        }else{
            throw new Error('Error al obtener inmuebles')
        }
    })

    .then (function(data){
        let tabla_inmuebles = document.getElementById('tabla_inmuebles');

        for(let inmueble of data){
            let fila = document.createElement('tr');

            fila.innerHTML = '<td>' + inmueble.id_inmueble + '</td>' +
                        '<td>' + inmueble.direccion + '</td>' +
                        '<td align="right">' + inmueble.localidad + '</td>' +
                        '<td align="right">' + inmueble.provincia + '</td>' + '<td>' + inmueble.codigo_precio + '</td>' +  '<td>' + inmueble.codigo_operacion + '</td>' +  '<td>' + inmueble.codigo_tipo_inmueble + '</td>' +  '<td>' + inmueble.codigo_estado_inmueble + '</td>' +'<td>' + inmueble.descripcion + '</td>';

                        tabla_inmuebles.append(fila);
        }
    })

    .catch(function(error){
        alert('Error al obtener inmuebles');
    });