function reassignUiElements() {
	$('.datepicker').datepicker(
		{
			dateFormat: "yy-mm-dd",
			changeMonth: true,
			changeYear: true,
			showAnim: "slideDown",
			defaultDate: new Date(),
			showButtonPanel: true,
			showOtherMonths: true,
			selectOtherMonths: true
		}
	);
	$('.timepicker').timepicker({
		timeFormat:	'hh:mm:ss',
		stepHour: 1,
		stepMinute: 5,
		defaultTime: 0,
		showAnim: "slideDown",
	});
}

function assignButtonElements(element) {
	subElements = ['ul.icons li', '.ui-button']

	for (i = 0; i < subElements.length; i++) {
		$(element).delegate(subElements[i], 'mouseover mouseout', function(event) {
			if (event.type == 'mouseover') {
				$(this).addClass('ui-state-hover');
			} else if (event.type == 'mouseout') {
				$(this).removeClass('ui-state-hover');
			}
		});
	}
}

function castDialog(model, action, properties, arguments) {
	$('<div/>', {
		id: model + '_' + action + '_dialog',
		title: properties.title
	}).appendTo('body');

	buttons = {}
	buttons[properties.OK] = function() {
		$('.error').html('');
		$('.ui-state-error').removeClass('ui-state-error');

		data = {}
		$('#' + model + '_' + action + ' input').each(function(i, el) {
			data[$(el).attr('id')] = $(el).val();
		});
		$('#' + model + '_' + action + ' select').each(function(i, el) {
			data[$(el).attr('id')] = $(el).val();
		});
		console.log(data);
		$.ajax("/" + model + "/ajax/" + action, {
			type: 'post',
			data: data
		}).done(function(response) {
			if (action == 'new' || action == 'edit') {
				if (response['id']) {
					newEl = null;
					if (action == 'edit') {
						newEl = $("#" + model + "_" + response['id']);
						newEl.html($("." + model + ".overflow").html());
					} else if (action == 'new') {
						newEl = $("." + model + ".overflow").clone();
					}

					// Conditional blocks (positive)
					var conditionalsRegExp=/\?\|(.+?)\|\?/g;
					results = newEl.html().match(conditionalsRegExp);

					if (results) {
						for (i = 0; i < results.length; i += 2) {
							variableName = results[i].substr(2, results[i].length-4);
							var innerConditionalRegExp = new RegExp("\\?\\|" + variableName + "\\|\\?", "g");

							innerConditionalRegExp.exec(newEl.html());
							var begin = innerConditionalRegExp.lastIndex;

							innerConditionalRegExp.exec(newEl.html());
							var end = innerConditionalRegExp.lastIndex;

							if ($('#' + variableName).val() == "" || $('#' + variableName).val() == undefined) {
								newEl.html(newEl.html().substr(0, begin) + newEl.html().substr(end));
							}

							newEl.html(newEl.html().replace(innerConditionalRegExp, ""));
						}
					}

					// Conditional blocks (negative)
					var conditionalsRegExp=/:\|(.+?)\|:/g;
					results = newEl.html().match(conditionalsRegExp);

					if (results) {
						for (i = 0; i < results.length; i += 2) {
							variableName = results[i].substr(2, results[i].length-4);
							var innerConditionalRegExp = new RegExp(":\\|" + variableName + "\\|:", "g");

							innerConditionalRegExp.exec(newEl.html());
							var begin = innerConditionalRegExp.lastIndex;

							innerConditionalRegExp.exec(newEl.html());
							var end = innerConditionalRegExp.lastIndex;

							console.log(variableName);
							console.log($('#' + variableName).val());

							if ($('#' + variableName).val() != "" && $('#' + variableName).val() != undefined) {
								newEl.html(newEl.html().substr(0, begin) + newEl.html().substr(end));
							}

							newEl.html(newEl.html().replace(innerConditionalRegExp, ""));
						}
					}

					// Variable replacement
					var placeholdersRegExp=/\*\|(.+?)\|\*/g;
					results = newEl.html().match(placeholdersRegExp);

					if (results) {
						for (i = 0; i < results.length; i++) {
							if (results[i].substr(2,2) == 'id') {
								newEl.attr('id', model + '_' + response['id']);
								newEl.html(newEl.html().replace(/\*\|id\|\*/g, ""+response['id']));
								newEl.html(newEl.html().replace(/\*%7Cid%7C\*/g, ""+response['id']));
							} else {
								variableName = results[i].substr(2, results[i].length-4);
								var currentPlaceholderRegex = new RegExp("\\*\\|" + variableName + "\\|\\*", "g");
								
								var variableValue = $('#' + variableName).val();
								if (variableValue == undefined) {
									newEl.html(newEl.html().replace(currentPlaceholderRegex, response[variableName]));
								} else {
									newEl.html(newEl.html().replace(currentPlaceholderRegex, variableValue));
								}
							}
						}
					}

					$("." + model + ".nothing").hide();

					if (properties['beforeDone']) {
						newEl = properties.beforeDone(response, newEl);

					}

					if (action == 'new') {
						newEl.insertBefore($("." + model + ".overflow")).fadeIn().removeClass("overflow");
					}

					$("#" + model + '_' + action + '_dialog').dialog("close");
					$("#" + model + '_' + action + '_dialog').remove();
				} else {
					for (value in response) {
						$('.' + value + ' .error').html(response[value]);
						$('#' + value).addClass('ui-state-error');
					}
				}
			} else if (action == 'delete') {
				if (properties['beforeDone']) {
					var element = $("#" + model + "_" + data[model + "_id"]);
					console.log(element);
					properties.beforeDone(response, element);
				}

				$("#" + model + "_" + data[model + "_id"]).fadeOut();

				$("#" + model + '_' + action + '_dialog').dialog("close");
				$("#" + model + '_' + action + '_dialog').remove();
			}
		});
	}

	buttons[properties.Cancel] = function() {
		$("#" + model + '_' + action + '_dialog').dialog("close");
		$("#" + model + '_' + action + '_dialog').remove();
	}

	$("#" + model + '_' + action + '_dialog').dialog({
		autoOpen: false,
		height: properties.height,
		width: properties.width,
		modal: properties.modal,
		resizable: properties.resizable,
		buttons: buttons,
		close: function() {
			if (properties['beforeClose']) {
				properties.beforeClose();
			}
			$(this).dialog("close");
			$("#" + model + '_' + action + '_dialog').remove();

		}
	});

	$("#" + model + '_' + action + '_dialog')
	.load("/" + model + "/ajax/" + action, arguments,
		function() {
			reassignUiElements();
			$(this).dialog("open");
		}
	);
}