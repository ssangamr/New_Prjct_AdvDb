<p>Todo List</p>
<p>This is not Development Server</p>
<table border="1">
%for row in rows:
    <tr>
    %for item in row:
        <td>{{item}}</td>
    %end
        <td>
            <a href="/delete_item/{{row[0]}}">DELETE</a>
        </td>
    </tr>
%end
</table>
<a href="/new_item">New Item...</a>