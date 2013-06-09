%def tree(points, level, counters):
	%if len(counters) <= level:
		%counters.append(1)
	%else:
		%counters[level] = 1
	%end

	%for point in points:
		<div class="points level{{level}}">
			<div id="point_{{point['id']}}" class="point">
				<p class="text">
					<span class="number">
					%number = ""

					%for r in range(level+1):
						%number += str(counters[r]) + "."
					%end

					{{number}}
					</span>
					&nbsp;
					<span class="title">{{point['title']}}</span>
					%if point['description']:
						&mdash; <span class="description">{{point['description']}}</span>
					%end
				</p>
				<ul class="icons ui-widget ui-helper-clearfix">
					<li class="ui-state-default ui-corner-all"><a href="/point/edit/{{point['id']}}" class="point edit" data-rel="{{point['id']}}" title="Edit"><span class="ui-icon ui-icon-pencil"></span></a></li>
					<li class="ui-state-default ui-corner-all"><a href="/point/delete/{{point['id']}}" class="point delete" data-rel="{{point['id']}}" title="Delete"><span class="ui-icon ui-icon-trash"></span></a></li>
				</ul>
			</div>

			%if 'subpoints' in point and point['subpoints']['count']:
				%tree(point['subpoints']['rows'], level+1, counters)
			%end
		</div>
		%counters[level] += 1
	%end
%end
<div class="odj">
	<h2>Agenda</h2>
	<div class="buttons"><button class="new point ui-button ui-widget ui-state-default ui-corner-all ui-button-text-only"><!--<a href="/point/new">--><span class="ui-button-text">New Point</span><!--</a>--></button></div>
	%if points['count']:
		%tree(points['rows'], 0, list())
	%else:
		<div class="nothing point">
			<span>No point.</span>
		</div>
	%end
	<div class="point overflow">
		<p class="text">
			<span class="number">
			*|number|*
			</span>
			&nbsp;
			<span class="title">*|title|*</span>?|description|?
				&mdash; <span class="description">*|description|*</span>?|description|?
		</p>
		<ul class="icons ui-widget ui-helper-clearfix">
			<li class="ui-state-default ui-corner-all"><a href="/point/edit/*|id|*" class="point edit" data-rel="*|id|*" title="Edit"><span class="ui-icon ui-icon-pencil"></span></a></li>
			<li class="ui-state-default ui-corner-all"><a href="/point/delete/*|id|*" class="point delete" data-rel="*|id|*" title="Delete"><span class="ui-icon ui-icon-trash"></span></a></li>
		</ul>
	</div>
</div>
<script type="text/javascript">
	$(document).ready(function() {
		$(".point.new").click(function(e) {
			e.preventDefault();
			properties = {
				title:"New Point",
				OK:"Create",
				Cancel:"Cancel",
				width:200,
				height:280,
				modal:true,
				resizable:false,
				beforeDone: function(response, element) {
					if (response['parent_id'] == "") {
						wrapperEl = $('<div class="overflow points level0"></div>');
						element.removeClass('overflow');
						wrapperEl.append(element);

						return wrapperEl;
					}

					return element;
				}
			}
			castDialog('point', 'new', properties, null);
		});
		$(".odj").delegate(".point.edit", "click", function(e) {
			e.preventDefault();
			properties = {
				title:"Edit Point",
				OK:"Edit",
				Cancel:"Cancel",
				width:200,
				height:280,
				modal:true,
				resizable:false
			}
			castDialog('point', 'edit', properties, "point_id=" + $(this).attr('data-rel'));
		});
		$(".odj").delegate(".point.delete", "click", function(e) {
			e.preventDefault();
			properties = {
				title:"Are you sure you want to delete this point ?",
				OK:"Yes",
				Cancel:"No",
				width:320,
				height:125,
				modal:true,
				resizable:false,
				beforeDone: function(response, element) {
					$(element).next('.points').fadeOut();

					return element;
				}
			}
			castDialog('point', 'delete', properties, "point_id=" + $(this).attr('data-rel'));
		});
	});
</script>