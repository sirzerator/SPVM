		%def tree(points, level, counters):
			%if len(counters) <= level:
				%counters.append(1)
			%else:
				%counters[level] = 1
			%end

			%for point in points:
				<div class="point level{{level}}">
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

					<ul class="icons ui-widget ui-helper-clearfix">
						<li class="ui-state-default ui-corner-all"><a href="/point/edit/{{point['id']}}" class="point edit" rel="{{point['id']}}" title="Edit"><span class="ui-icon ui-icon-pencil"></span></a></li>
						<li class="ui-state-default ui-corner-all"><a href="/point/delete/{{point['id']}}" class="point delete" rel="{{point['id']}}" title="Delete"><span class="ui-icon ui-icon-trash"></span></a></li>
					</ul>

					%if 'children' in point and point['children']['count']:
						%tree(point['children']['rows'], level+1, counters)
					%end
				</div>
				%counters[level] += 1
			%end
		%end
		<h1>SPVM</h1>
		<div class="controls">
			<span class="configuration"></span>
			<span class="quit"><a href="/pv/close">Close</a></span>
		</div>
		<h2>{{pv_data['title']}}</h2>
		<div class="informations toggle">
			<div class="location">{{pv_data['location']}}</div>
			<div class="date time">{{pv_data['date']}} {{pv_data['time']}}</div>
			<div class="description">{{pv_data['description']}}</div>
			<div class="modified">{{pv_data['modified']}}</div>
		</div>
		<div class="points left">
			<p class="buttons"><a href="/point/new" class="button new point"><button class="ui-button ui-widget ui-state-default ui-corner-all ui-button-text-only"><span class="ui-button-text">New Point</span></button></a></p>
			%if points['count']:
				%tree(points['rows'], 0, list())
			%else:
				<div class="ajax point">
					<span class="number">1.</span>
					<input class="title placeholder" value="Click here to add a new point" />
				</div>
				<div class="overflow point">
					<span class="number">1.</span>

				</div>
			%end
		</div>
		<script type="text/javascript">
			$(document).ready(function() {
				assignButtonElements($('body'));
			});
		</script>
		%rebase layout title='SPVM'