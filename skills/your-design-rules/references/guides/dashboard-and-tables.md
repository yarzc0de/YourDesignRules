# Dashboards and tables guide

Rules for dashboards, reports, analytics views, and data tables, in any stack (HTML and CSS, React,
SwiftUI, Flutter). Read it after `references/rules/core.md` whenever a screen's main job is showing metrics, charts, or
records. Buttons and forms are in `references/guides/web-app.md`; chart colors and contrast in `references/rules/color.md`; number
typography in `references/rules/typography.md`.

## Purpose

### DATA-1 · Start from the question the screen answers
Before any layout, write down the one question this view answers for its main user ("Are we on track for
this month's sales target?"). Every metric, chart, and table must help answer it or its obvious follow-up;
material that serves another question belongs in another view (CORE-1).
- **Why:** a dashboard built from "all the data we have" answers nothing.
- **Check:** for each element you can say which part of the question it answers.

### DATA-2 · Make one metric or chart the hero
Pick the single number or chart that answers the question and give it the most space and the strongest
position: first in reading order, largest value, or widest panel. Supporting metrics are visibly smaller.
Never lay out eight KPI tiles of equal size and weight.
- **Why:** equal tiles make the user work out importance alone (CORE-2).
- **Check:** squint at the render; one number or chart stands out before anything else.

### DATA-3 · Give every metric a label, value, and context
A bare number is not a metric. Build each one from these parts:

| Part | Spec | Example |
|---|---|---|
| Label | 12–14, weight 500, muted, sentence case | Active subscriptions |
| Value | 28–40 (hero 48–64), weight 600–700, tabular figures | 4,180 |
| Unit | smaller and quieter than the value | %, ms, k |
| Delta | sign, arrow, and color together, never color alone | +3.2% |
| Comparison basis | what the delta is measured against | vs. previous 30 days |
| Period | the time window the value covers | Oct 1–31 |
| Sparkline (optional) | 24–40 tall, no axes, same period as the value | |

Color a delta by whether the change is good, not by its direction: rising churn is a warning. Keep a metric
strip to 3–5 items; anything beyond that belongs in a table.
- **Why:** without a period and a comparison, nobody can tell whether a number is good.
- **Check:** each value on screen shows its unit, its period, and what it is compared with.

## Charts

### DATA-4 · Choose the chart type from the question
Default to a bar chart for comparing items and a line chart for change over time.

| Question | Use | Avoid |
|---|---|---|
| How do categories compare? | bar chart sorted by value; horizontal when labels are long | pie, radar, 3D bars |
| How did a value change over time? | line chart; columns for ≤ 12 discrete periods | smoothed curves that imply values between points |
| What share does each part take, ≤ 4 parts? | donut or 100% stacked bar | pie or donut with 5+ slices |
| What share does each part take, 5+ parts? | sorted bar chart | donut, pie |
| How are values distributed? | histogram or box plot | a single average |
| Are two measures related? | scatter plot | dual-axis line chart |
| How do items rank? | sorted bar chart or ranked table | unsorted bars, bubble chart |
| Are we on track to a target? | progress or bullet bar with a target marker | gauge or speedometer dial |
| How did the mix change over time? | stacked bars or stacked area, ≤ 4 series | 6+ stacked series, streamgraph |
| What is the exact value for one item? | table | any chart |

- **Why:** the right form makes the answer visible without reading the numbers.
- **Check:** you can name the question each chart answers, and it matches its row here.

### DATA-5 · Give each chart one insight and highlight it
When the data supports a finding, state it in the title ("Signups fell after the March price change") or in
a one-line takeaway. Draw the key series or point in the highlight color and the rest in neutrals from the
colorblind-safe palette in `references/rules/color.md`, and label the highlighted value directly.
- **Why:** a chart without a stated point leaves each viewer to find a different one.
- **Check:** the title states a finding, and exactly one series or point carries the highlight color.

### DATA-6 · Strip chart junk
- Gridlines: few, light, horizontal only, or none when values are labeled.
- No 3D, bevels, drop shadows, or gradient fills on bars, lines, or slices.
- Direct labels at line ends or bar tips instead of a legend when there are ≤ 4 series.
- Bar axes start at zero; line axes may zoom in but label the range clearly.
- Axis and data labels ≥ 12 in tabular figures, with one number format (decimals, units) per chart.
- **Why:** every mark that is not data competes with the data for attention.
- **Check:** remove each decoration in turn; if the chart reads the same, leave it out.

### DATA-7 · Render charts with a library or real SVG
Use a charting library (Recharts, Chart.js, ECharts, Vega-Lite, Swift Charts, fl_chart) or computed SVG
paths. Never place dots, bars, or labels by hand, and never absolutely position text over a chart; let the
library or the layout tie labels to data. Charts are live elements, never images (CORE-10).
- **Why:** hand-placed marks drift away from the data and break on resize.
- **Check:** change one data value; both the mark and its label move.

### DATA-8 · Plot only data you were given
Do not invent series, trend lines, forecasts, benchmarks, or previous-period comparisons the user did not
supply (CORE-9). If the design needs a chart and no data exists, use an obvious sample (DATA-18) and label
the chart "Sample data".
- **Why:** an invented series reads as fact and ships as fact.
- **Check:** every series traces to the brief or carries a sample label (CHK-10).

## Table structure

### DATA-9 · Nest table, row, cell, then content
A table holds rows, rows hold cells, cells hold content: text, a badge, an avatar, a button. The cell is
the container that owns column width, padding, and alignment; content never sits directly in a row. Use real
table markup, or a grid whose column template is defined once and shared by the header and every row.

**Avoid:** values dropped straight into a flex row, so each row sizes itself from its own text.
```html
<div class="row">
  Northwind Ltd <span class="badge">Active</span> Mar 12, 2026 $4,200 <button>More</button>
</div>
```
**Do:** every value in its own cell; widths come from the column definitions.
```html
<tr>
  <td class="col-name">Northwind Ltd</td>
  <td class="col-status"><span class="badge">Active</span></td>
  <td class="col-date">Mar 12, 2026</td>
  <td class="col-num">$4,200</td>
  <td class="col-actions"><button aria-label="Row actions">More</button></td>
</tr>
```
Grid version: set `grid-template-columns: minmax(200px, 250px) 112px 136px 104px 88px;` on the header and on
every row (or use `subgrid`).
- **Why:** shared cell geometry is what makes columns line up.
- **Check:** each column's edges form one straight line from the header to the last row.

### DATA-10 · Size columns by content type
| Column | Width | Align |
|---|---|---|
| Selection checkbox | 40–48 | center |
| Primary identifier (name, title, ID) | 200–250 | left |
| Person with avatar | 160–200 | left |
| Email, URL, description | flexible, fills the remaining space (min 160) | left |
| Status or badge | 100–120 | left, or center if used the same way everywhere |
| Date or time | 120–150 | left |
| Number, currency, percent | 80–120 | right |
| Actions | 80–100 | right |

Show 4–7 columns by default and move the rest into the detail view or a column picker. Truncate long text
with an ellipsis and expose the full value on hover, on focus, or in the detail view; a cell never spills
into its neighbor.
- **Why:** content-based widths keep scanning fast and stop one long value from reshaping the table.
- **Check:** with the longest realistic name and email loaded, the columns do not shift (CHK-2).

### DATA-11 · Align text left and numbers right
Text columns align left. Numeric columns align right and use tabular figures
(`font-variant-numeric: tabular-nums`) with the same number of decimals down the column. Put units in the
header ("Revenue (USD)") instead of repeating them in every cell. Each header aligns like its column's
content, and the status column keeps one alignment across the product.
- **Why:** right-aligned tabular digits let people compare magnitudes by length at a glance.
- **Check:** the ones digits in each numeric column form one vertical line.

### DATA-12 · Pick one row density per table
| Density | Row height | Use |
|---|---|---|
| Compact | 36–40 | many rows, expert users, data-heavy screens |
| Default | 44–52 | most tables |
| Comfortable | 56–64 | rows with avatars or two-line cells |

Horizontal cell padding is 12–16, and the first and last cells line up with the padding of the header area
above. Separate rows with hairline dividers or with zebra striping, never both. One table uses one density.
- **Why:** a steady row height creates the rhythm the eye follows across a row.
- **Check:** all body rows share one height, and only one row-separation method is in use.

## Table frame and actions

### DATA-13 · Frame the table with header, body, and footer
- **Header area:** table title with the row count, search, filters, and the primary action on the right
  ("Add customer"). Active filters show as removable chips below it.
- **Column header:** labels 12–14, weight 500–600, muted; the sorted column shows its direction icon.
- **Body:** the rows, at one density (DATA-12).
- **Footer:** range and total ("1–25 of 312") plus pagination or a "Load more" control.
- **Sticky header:** pin the column header once the table scrolls past one viewport.
- **Why:** people need to know what they are looking at, how much of it there is, and how to narrow it.
- **Check:** scrolled to the middle of a long table, the column labels are still visible.

### DATA-14 · Put row actions in an overflow menu
Show at most one inline action per row, such as "Open" or a toggle; the rest go into an overflow menu in the
last column. If a row opens a record, make the whole row clickable with visible hover and focus states.
Destructive row actions sit last in the menu, styled as destructive, and confirm before running (CORE-11).
- **Why:** five icon buttons repeated on fifty rows are noise and an easy mis-click.
- **Check:** no row shows more than one inline action plus the overflow trigger.

### DATA-15 · Show bulk actions only after selection
Add a checkbox column (40–48 wide) with select-all in the column header. Once a row is selected, a bulk bar
replaces or overlays the header area: the selected count ("3 selected"), the bulk actions, and a control that
clears the selection. Bulk destructive actions confirm with the count ("Delete 3 invoices").
- **Why:** bulk actions shown all the time clutter the frame and look usable with nothing chosen.
- **Check:** with zero rows selected, no bulk action is visible.

## States

### DATA-16 · Design every data state
Each table, chart, and metric gets all of these states, drawn on purpose rather than left to chance (CHK-9).

| State | Show |
|---|---|
| Loading | 5–8 skeleton rows or chart placeholders matching the final layout; header and frame stay in place |
| Empty, no data yet | one sentence on what will appear here, plus the primary action that creates it |
| No results for a filter | the active filter or query by name, plus "Clear filters" |
| Error | what failed in plain words, plus "Retry"; keep any data that already loaded |
| Partial or stale | last-updated time ("Updated 6 min ago") and a refresh control |
| No permission | what is restricted and who can grant access |

- **Why:** a blank table looks broken, and users cannot tell "nothing here" from "something failed".
- **Check:** each state has its own frame or toggle in the design.

## Mobile

### DATA-17 · Collapse wide tables into list rows on phones
Below about 640 wide, turn each row into a list row, or a card when records are selectable objects, showing
the 2–3 fields that matter most: the primary identifier as the title, status as a badge, one key number on
the right, and an optional muted second line. Tapping opens the full record. Keep sideways scrolling only
when comparing across columns is the point, and then freeze the first column.
- **Why:** a seven-column table at 375 wide can be neither read nor tapped.
- **Check:** at 375 each record reads without sideways scrolling, and its tap target is ≥ 44 tall.

## Sample data

### DATA-18 · Make sample data realistic and label it
When no data is supplied, fill tables and charts with plausible values: varied name lengths, dates within
one realistic range, every status value represented, numbers of a believable magnitude. Use generic names,
never real companies or people. Label the surface "Sample data" and say so in your reply (CORE-9).
- **Why:** uniform filler hides the layout bugs that real data will expose.
- **Check:** the longest name, the largest number, and every status value appear at least once.

## Dashboard skeleton

### DATA-19 · Use the default skeleton only when it fits
When the task really is an operational dashboard, this arrangement is a sound starting point:

```
+------------+--------------------------------------------------+
|            | Breadcrumbs                                      |
| Navigation | Page title                [Date range] [Action]  |
|            +--------------------------------------------------+
|            | Hero metric     Metric     Metric     Metric     |
|            +-------------------------------+------------------+
|            | Primary chart (8 of 12 cols)  | Supporting (4)   |
|            +-------------------------------+------------------+
|            | Table (full width)                               |
+------------+--------------------------------------------------+
```

- **Navigation:** sidebar 240–280 wide, or a top bar 56–64 tall when there are six destinations or fewer.
- **Spacing:** page padding 24–32, gaps between regions 24–32, panel padding 24 (`references/rules/layout.md`).
- **Metric strip:** one surface divided by hairlines usually beats separate tiles (CORE-6).

Do not assume this skeleton. A single-question report may be one chart and a table; a monitoring wall may be
all charts; a phone summary may be a list. Start from DATA-1 and keep only the regions the question needs.
- **Why:** the generic admin template shows up whether or not anyone needs a sidebar and four tiles.
- **Check:** every region on the screen maps to a part of the question written for DATA-1.

## Review

Run `references/rules/review-checklist.md` on each region, with extra care for CHK-2, CHK-9, CHK-10, and CHK-12.
