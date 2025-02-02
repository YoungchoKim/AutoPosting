def dict_to_html(data):
    html = ""
    for key, value in data.items():
        html += f"<h3>{key.title()}</h3>\n<ul>\n"
        for line in value.split('. '):
            if line.strip():
                html += f"    <li>{line.strip()}</li>\n"
        html += "</ul>\n"
    return html

def tistory_code_block(code):
    html = "<h3>Solution Code:</h3>\n"
    html += "<pre><code>\n"
    for line in code.split('\n'):
        html += f"<code>{line}</code>\n"
    html += "</code></pre>\n"
    return html


if __name__ == "__main__":
    data = {
        'summary': 'Finding the redundant edge in a graph that becomes a tree after removing one edge',
        'approach': 'The solution uses a disjoint set data structure to keep track of connected components in the graph. It iterates through the edges and checks if the two nodes of each edge are in the same connected component. If they are not, it merges the two components. If they are, it means the edge is redundant and the solution returns it.',
        'complexity': 'O(n * alpha(n)) where n is the number of nodes in the graph and alpha(n) is the inverse Ackermann function, which grows very slowly. In practice, the time complexity is close to O(n)',
        'explain': 'The solution starts by initializing the disjoint set data structure with each node as its own parent. It then iterates through the edges and checks if the two nodes of each edge are in the same connected component. If they are not, it merges the two components by making the root of one component the parent of the other. If they are, it means the edge is redundant and the solution returns it. The disjoint set data structure allows the solution to efficiently check if two nodes are in the same connected component and to merge two components.'
    }

    # Generate HTML
    html_output = dict_to_html(data)
    print(html_output)