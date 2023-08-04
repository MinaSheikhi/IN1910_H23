from typing import Any

import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch


def make_fig(figsize=(12, 6)):
    fig = plt.figure(figsize=figsize)
    plt.axis("off")
    plt.xlim(0, 1)
    plt.ylim(0, 1)
    return fig


def save(filename):
    plt.tight_layout()
    plt.savefig(f"figures/{filename}.png")


def get_edge(box, edge=""):
    edge = edge.split()
    x, y = box["x"], box["y"]
    if "right" in edge:
        x += box["width"] / 2
    elif "left" in edge:
        x -= box["width"] / 2
    if "upper" in edge:
        y += box["height"] / 2
    elif "lower" in edge:
        y -= box["height"] / 2
    return (x, y)


def add_box(box):
    edge = (box["x"] - box["width"] / 2, box["y"] - box["height"] / 2)
    rectangle = plt.Rectangle(
        edge,
        box["width"],
        box["height"],
        facecolor=box["color"],
        edgecolor="black",
        fill=True,
        linewidth=2,
    )
    plt.gca().add_patch(rectangle)
    plt.text(
        box["x"],
        box["y"],
        box["text"],
        size=box["fsize"],
        ha="center",
        va="center",
    )


def add_note(box, text, corner="upper left", rotation=35, color="gainsboro"):
    """
    Add note to box
    """
    x, y = get_edge(box, corner)
    box = {"facecolor": color, "linewidth": 2}
    plt.text(
        x,
        y,
        "File Changes",
        rotation=rotation,
        size=work["fsize"],
        ha="center",
        va="center",
        bbox=box,
    )


def add_boxes(boxes):
    for box in boxes:
        add_box(box)


def add_empty_boxes(boxes):
    if isinstance(boxes, dict):
        boxes = [boxes]
    for box in boxes:
        empty = box.copy()
        empty["text"] = ""
        add_box(empty)


def add_arrow(r0, r1, arrow_type):
    """
    r0 : position of tail (float, float)
    r1 : position of head (float, float)
    arrow_type : 'double', 'curved' or 'straight' (default)
    """
    if arrow_type == "double":
        style = "<|-|>, head_width=8, head_length=8"
        arrow = FancyArrowPatch(r0, r1, arrowstyle=style, color="black")
    else:
        arc = "arc3,rad=-.1" if arrow_type == "curved" else "arc3,rad=0"
        style = "Simple, tail_width=1, head_width=8, head_length=8"
        arrow = FancyArrowPatch(
            r0,
            r1,
            connectionstyle=arc,
            arrowstyle=style,
            color="black",
        )
    plt.gca().add_patch(arrow)


def add_text_to_arrow(r0, r1, text, fsize, dx=0, dy=0, eps=1e-6):
    x0, y0 = r0
    x1, y1 = r1
    x, y = (x0 + x1) / 2, (y0 + y1) / 2
    if abs(y0 - y1) < eps:
        ha = "center"
    elif y0 > y1:
        ha = "left"
        x += dx
    else:
        ha = "right"
        x -= dx
    if abs(x0 - x1) < eps:
        va = "center"
    elif x0 > x1:
        va = "top"
        y -= dy
    else:
        va = "bottom"
        y += dy
    plt.text(x, y, text, size=fsize, ha=ha, va=va)


def add_curve(start, end, text=None, dx=0.01, dy=0.025, eps=1e-6):
    if start["y"] < end["y"]:
        edge_0 = "upper " + ("right" if start["x"] < end["x"] else "left")
        edge_1 = "lower " + ("right" if start["x"] > end["x"] else "left")
    elif start["y"] > end["y"]:
        edge_0 = "lower " + ("left" if start["x"] > end["x"] else "right")
        edge_1 = "upper " + ("left" if start["x"] < end["x"] else "right")
    else:
        edge_0 = "upper right" if start["x"] < end["x"] else "lower left"
        edge_1 = "upper left" if start["x"] < end["x"] else "lower right"
    r0 = get_edge(start, edge_0)
    r1 = get_edge(end, edge_1)
    add_arrow(r0, r1, arrow_type="curved")
    if text is not None:
        add_text_to_arrow(r0, r1, text, fsize=start["fsize"], dx=dx, dy=dy, eps=eps)


def _add_link(start, end, edges, text, dx, dy, eps, double_arrow):
    r0 = get_edge(start, edges[0])
    r1 = get_edge(end, edges[1])
    arrow_type = "double" if double_arrow else "straight"
    add_arrow(r0, r1, arrow_type=arrow_type)
    if text is not None:
        add_text_to_arrow(r0, r1, text, fsize=start["fsize"], dx=dx, dy=dy, eps=eps)


def add_vlink(start, end, text=None, dx=0.01, dy=0.025, eps=1e-6, double_arrow=False):
    edge_0 = "upper " if start["y"] < end["y"] else "lower"
    edge_1 = "lower " if start["y"] < end["y"] else "upper"
    _add_link(start, end, (edge_0, edge_1), text, dx, dy, eps, double_arrow)


def add_hlink(start, end, text=None, dx=0.01, dy=0.025, eps=1e-6, double_arrow=False):
    edge_0 = "right" if start["x"] < end["x"] else "left"
    edge_1 = "left" if start["x"] < end["x"] else "right"
    _add_link(start, end, (edge_0, edge_1), text, dx, dy, eps, double_arrow)


def add_commits(x0, y0, dx, hash_tags):
    K = len(hash_tags)
    commits = [get_commit(x0 + k * dx, y0, hash_tags[k]) for k in range(K)]
    add_box(commits[0])
    for k in range(K - 1):
        add_box(commits[k + 1])
        add_hlink(commits[k + 1], commits[k])
    return commits


def add_head(commit, dy):
    head = commit.copy()
    head["text"] = "HEAD"
    head["color"] = "coral"
    head["y"] += dy
    add_box(head)
    add_vlink(head, commit)


def add_branch(commit, dy, branch_name="main"):
    branch = commit.copy()
    branch["text"] = branch_name
    branch["color"] = "CornflowerBlue"
    branch["y"] += dy
    add_box(branch)
    add_vlink(branch, commit)
    return branch


status: dict[str, Any] = {"y": 0.7, "height": 0.25, "width": 0.175, "fsize": 25}
x_min = 0.175
x_max = 1 - status["width"]
x_mid = (x_min + x_max) / 2
work = {**status, **{"x": x_min, "text": "Working\nDirectory", "color": "powderblue"}}
stage = {**status, **{"x": x_mid, "text": "Staging\nArea", "color": "LemonChiffon"}}
repo = {**status, **{"x": x_max, "text": "Repository", "color": "seagreen"}}

y_down = 0.2
untrack = {
    **status,
    **{"x": x_min, "y": y_down, "text": "Untracked", "color": "gainsboro"},
}
trash = {**status, **{"x": x_min, "y": y_down, "text": "", "color": "indianred"}}

commit_box = {"height": 0.117, "width": 0.125, "fsize": 25, "color": "thistle"}
get_commit = lambda x, y, hash_tag: {**{"x": x, "y": y, "text": hash_tag}, **commit_box}

if __name__ == "__main__":
    make_git_figures = True
    make_branch_figures = True
    if make_git_figures:
        make_fig()
        add_boxes([work, stage, repo])
        save("areas")
        add_curve(work, stage, "git add")
        save("add")
        add_curve(stage, repo, "git commit")
        save("commit")
        add_note(work, "File Changes")
        save("changes")
        plt.close()

        make_fig()
        add_boxes([work, stage, repo, trash])
        add_curve(work, stage, "git add")
        add_curve(work, trash, "git restore")
        save("restore")
        plt.close()

        make_fig()
        add_boxes([work, stage, repo])
        add_curve(work, stage, "git add")
        add_curve(stage, work, "git restore --staged")
        save("restore-staged")
        plt.close()

        make_fig()
        add_boxes([work, stage, repo, untrack])
        save("stages")
        add_curve(work, stage, "git add")
        add_curve(untrack, stage, "git add")
        add_curve(stage, repo, "git commit")
        save("untracked")
        plt.close()

        make_fig()
        add_empty_boxes([work, stage, repo, untrack])
        save("empty")
        plt.close()

        make_fig()
        add_boxes([work, stage, repo])
        add_hlink(work, stage, "git diff", double_arrow=True)
        add_hlink(stage, repo, "git diff\n--cached", double_arrow=True)
        save("diff")
        plt.close()

    if make_branch_figures:
        dx = 1.5 * commit_box["width"]  # type: ignore
        dy = 1.5 * commit_box["height"]  # type: ignore
        x0, y0 = 0.1, 0.5

        K = 5
        tags = [f"#{k+1}" for k in range(K)]
        make_fig()
        commits = add_commits(x0, y0, dx, hash_tags=tags)
        main = add_branch(commits[-1], dy)
        add_head(main, dy)
        save("log")
        plt.close()

        make_fig()
        commits = add_commits(x0, y0, dx, hash_tags=tags)
        main = add_branch(commits[-1], dy)
        add_head(commits[2], dy)
        save("checkout")
        plt.close()

        make_fig()
        commits = add_commits(x0, y0, dx, hash_tags=tags[:3])
        main = add_branch(commits[-1], dy)
        add_head(main, dy)
        save("reset")
        plt.close()

        make_fig()
        tags = [""]
        commits = add_commits(x0, y0, dx, hash_tags=tags * 3)
        main = add_branch(commits[-1], dy)
        testing = add_branch(commits[-1], -dy, branch_name="testing")
        add_head(main, dy)
        save("new_branch")
        plt.close()

        make_fig()
        tags = [""]
        commits = add_commits(x0, y0, dx, hash_tags=tags * 3)
        main = add_branch(commits[-1], dy)
        testing = add_branch(commits[-1], -dy, branch_name="testing")
        add_head(testing, -dy)
        save("switch")
        plt.close()

        make_fig()
        tags = [""]
        commits = add_commits(x0, y0, dx, hash_tags=tags * 4)
        main = add_branch(commits[-2], dy)
        testing = add_branch(commits[-1], -dy, branch_name="testing")
        add_head(testing, -dy)
        save("advance")
        plt.close()

        make_fig()
        tags = [""]
        commits = add_commits(x0, y0, dx, hash_tags=tags * 4)
        main = add_branch(commits[-2], dy)
        testing = add_branch(commits[-1], -dy, branch_name="testing")
        add_head(main, dy)
        save("advance-switch")
        plt.close()

        make_fig()
        stem = add_commits(x0, y0, dx, hash_tags=tags * 3)
        main_commits = add_commits(stem[-1]["x"] + dx, y0 + dy / 2, dx, hash_tags=tags)
        test_commits = add_commits(
            stem[-1]["x"] + dx,
            y0 - dy / 2,
            dx,
            hash_tags=tags * 2,
        )
        add_hlink(main_commits[0], stem[-1])
        add_hlink(test_commits[0], stem[-1])
        main = add_branch(main_commits[-1], dy)
        testing = add_branch(test_commits[-1], -dy, branch_name="testing")
        add_head(main, dy)
        save("diverge_main")
        plt.close()

        make_fig()
        stem = add_commits(x0, y0, dx, hash_tags=tags * 3)
        main_commits = add_commits(stem[-1]["x"] + dx, y0 + dy / 2, dx, hash_tags=tags)
        test_commits = add_commits(
            stem[-1]["x"] + dx,
            y0 - dy / 2,
            dx,
            hash_tags=tags * 2,
        )
        add_hlink(main_commits[0], stem[-1])
        add_hlink(test_commits[0], stem[-1])
        main = add_branch(main_commits[-1], dy)
        testing = add_branch(test_commits[-1], -dy, branch_name="testing")
        add_head(testing, -dy)
        save("diverge_testing")
        plt.close()
