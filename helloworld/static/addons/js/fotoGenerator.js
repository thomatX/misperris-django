function generatePhoto(pk,foto,nombre) {
	$('body').append('<div class="modal fade" id="perro-'+pk+'" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel" aria-hidden="true">'+
						'<div class="modal-dialog" role="document">'+
							'<div class="modal-content">'+
							'<div class="modal-header">'+
								'<h5 class="modal-title" id="exampleModalLabel">'+nombre+'</h5>'+
								'<button type="button" class="close" data-dismiss="modal" aria-label="Close">'+
								'<span aria-hidden="true">&times;</span>'+
								'</button>'+
							'</div>'+
							'<div class="modal-body"> <img src="media/img/rescatados/'+foto+'"> </div>'+
							'<div class="modal-footer">'+
								'<button type="button" class="btn btn-secondary" data-dismiss="modal">Close</button>'+
							'</div>'+
							'</div>'+
						'</div>'+
						'</div>');
	return false;
}
