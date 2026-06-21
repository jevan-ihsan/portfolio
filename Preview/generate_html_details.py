import os
import re

md_path = "/Users/jevanhava/Documents/Project/Portofolio/Preview/python-data-analysis.md"
with open(md_path, "r", encoding="utf-8") as f:
    content = f.read()

# Split content by Part headers
parts_raw = re.split(r'\n## Part \d+:', content)

# A mapping of section titles in Part 4 to their respective charts and descriptions
images_map = {
    "Plot Single Variable Histogram": ("chart_histogram.png", "A histogram shows how often values fall into different ranges. Here, SPY returns form a tall, narrow peak centered around 0, showing that most daily changes are very small, with a few extreme return days on the outer edges."),
    "Adjusting Bin Count": ("chart_histogram.png", "Increasing the bin count to 50 breaks returns into narrower intervals. This gives a higher resolution view of the distribution, confirming that daily returns are highly symmetric and concentrated around zero."),
    "Dodge Comparison Plot": ("chart_histogram.png", "This side-by-side bar comparison shows that USO (Oil) returns have a much wider and flatter distribution compared to SPY and TLT, meaning oil daily returns are significantly more volatile."),
    "Layer Comparison Plot": ("chart_histogram.png", "Overlays the return distributions of SPY and TLT. This shows that the spread of SPY is slightly wider than TLT, meaning the S&P 500 experienced higher daily variance compared to US Treasury bonds during this period."),
    "Box Plot Comparison": ("chart_boxplot.png", "A box plot shows the median (line inside the box), the interquartile range (the box itself), and outliers (points beyond the whiskers). Here, the large spread of dots for USO confirms it has the highest volatility and the most extreme outlier returns, while TLT has the tightest range."),
    "Sliced Box Plot Comparison": ("chart_boxplot.png", "Comparing only SPY and TLT shows that while their medians are close to zero, the S&P 500 (SPY) has a slightly taller box (higher volatility) and more frequent extreme positive and negative outlier return days."),
    "Pairplot Grid": ("chart_pairplot.png", "A pairplot shows pairwise relationships across the entire dataset. The diagonal histograms show each asset's return spread, while the scatter plots show how assets move relative to each other. For example, the scatter plot of SPY vs TLT shows a round cloud, indicating very low correlation."),
    "Heatmap Visualizations": ("chart_heatmap.png", "A heatmap colors correlation coefficients to highlight relationships. The values close to 1 on the diagonal show each asset against itself. The correlation of -0.01 between SPY and TLT confirms US stocks and treasury bonds were uncorrelated during this period, while SPY and USO have a moderate positive correlation (0.45)."),
    "Baseline Line Plot": ("chart_linechart.png", "A line chart tracks continuous trends over time. This basic plot tracks the daily adjusted closing price of SPY, showing a general upward trend from around $360 to over $460, despite short-term dips."),
    "Styled Line Chart with Labels": ("chart_linechart.png", "Adding a title and axis labels makes the chart self-contained. The x-axis dates are rotated 45 degrees so they are readable without overlapping."),
    "Adjusting Plot Sizing & Line Color": ("chart_linechart.png", "Setting the figure size to 14x5 stretches the timeline for easier scanning, and changing the line color to a custom shade makes the visual look clean and professional."),
    "Custom Dotted Red Line Chart": ("chart_linechart.png", "Using circular markers and a red dotted line style is useful when you want to highlight discrete data points along the continuous timeline."),
    "Adjusting Axis Slicing (Limits)": ("chart_linechart.png", "Setting the y-axis limits to zoom in between $340 and $500 removes empty vertical space, making it much easier to inspect the price fluctuations."),
    "Convert Mean Values for Bar Plot": ("chart_barplot.png", "Before plotting, we compile the average price of each asset into a summary DataFrame. This step calculates that SPY has the highest average price, followed by TLT, and USO has the lowest."),
    "Basic Vertical Bar Plot": ("chart_barplot.png", "A vertical bar plot is best for comparing absolute values of different categories. Here, we compare the mean prices of SPY, TLT, and USO side-by-side."),
    "Styled Bar Charts (Palettes)": ("chart_barplot.png", "Applying the 'coolwarm' palette styles the bars with a color gradient, making the differences between categories more visually distinct."),
    "Horizontal Bar Plot": ("chart_barplot.png", "Horizontal bars are ideal when you have long category labels. It displays the same mean price comparisons rotated 90 degrees."),
    "Horizontal Bar Plot with Annotation Text": ("chart_barplot.png", "Adding an annotation text callout directly on the chart immediately highlights the key takeaway: SPY's mean price is significantly higher ($409) than TLT's and USO's."),
    "Basic Scatter Plot": ("chart_scatter.png", "A scatter plot plots two continuous variables against each other to look for relationships. The circular cloud of points for SPY vs TLT returns confirms their near-zero correlation."),
    "Add Year Dimension Column": ("chart_scatter.png", "To analyze how relationships change over time, we add a 'Year' column to the dataset to use as a categorical styling variable."),
    "Scatter Plot with Style Categorical Coding": ("chart_scatter.png", "Using different marker shapes (circles, squares, triangles) for each year helps distinguish the time periods, though it can look cluttered with many points."),
    "Scatter Plot with Hue Color Coding": ("chart_scatter.png", "Coloring the points by year is a much cleaner way to see if returns clustered differently in certain years. The overlapping colors show the general relationship remained stable across years."),
    "Scatter Plot with Size Bubble Coding": ("chart_scatter.png", "Sizing the points by year creates a bubble chart. Here, the larger bubbles represent more recent years, though this is usually better suited for continuous variables like trading volume."),
    "Multi-Dimensional Scatter Plot": ("chart_scatter.png", "This scatter plot visualizes four variables at once: x/y coordinate for SPY vs TLT returns, color hue for the year, and bubble size for USO (Oil) returns. It shows that large daily swings in oil prices (larger bubbles) occur randomly across all years and return ranges."),
    "Discrete Frequency Histogram of Order Quantities": ("chart_ex_histogram.png", "This histogram tracks customer order quantities from our transaction log. The peak at 1 and 2 shows that the vast majority of orders are small-quantity purchases, which drops off sharply for larger order counts."),
    "Grouped Order Counts per Customer": ("chart_ex_barplot.png", "This bar chart groups our customer base by their total order frequency. It reveals that most customers only placed a single order, highlighting a key business opportunity to improve repeat customer retention."),
    "Bivariate Scatter Plot: Quantity vs. Amount": ("chart_ex_scatterplot.png", "This scatter plot compares order quantity against the total transaction amount. The distinct horizontal bands show price tiers, confirming that total spending scales linearly with quantity but is bounded by standard product pricing.")
}

walkthrough_intro = {
    1: '''  <p>I started with the basics of Python syntax. I wanted to understand how different data structures work and when to use them. This part covers variables, basic syntax, and flow control:</p>
  <ul>
    <li><strong>Lists:</strong> Used for ordered items that need to be changed or sorted, like names or numbers.</li>
    <li><strong>Tuples:</strong> Used for fixed values that should not be edited, preventing accidental bugs in the code.</li>
    <li><strong>Dictionaries:</strong> Used for fast key-value lookups where duplicate keys are not allowed.</li>
  </ul>''',
    2: '''  <p>This part focuses on importing data and cleaning it up. I pulled stock prices from online APIs and cleaned up messy local transaction files. In this section, I learned to:</p>
  <ul>
    <li><strong>Standardize tables:</strong> Rename columns for consistency and cast data to the correct types.</li>
    <li><strong>Handle missing data:</strong> Fill gaps using forward-fills for time-series data or medians to avoid skewing the dataset.</li>
    <li><strong>Clean duplicates and text:</strong> Drop duplicate rows and split text strings into separate columns.</li>
  </ul>''',
    3: '''  <p>Once the data was clean, I focused on manipulating tables to extract insights and run statistical checks:</p>
  <ul>
    <li><strong>Filter and slice:</strong> Extract specific records based on criteria (like high-performing engineering students).</li>
    <li><strong>Merge datasets:</strong> Combine tables using left joins to align student grades with their scholarships.</li>
    <li><strong>Statistical checks:</strong> Use Z-scores and IQR to find outliers, and build correlation matrices to see how variables move together.</li>
  </ul>''',
    4: '''  <p>This is where I turned raw numbers into visual charts. I split my plotting practice into two main categories:</p>
  <ul>
    <li><strong>Exploratory plots:</strong> Quick Seaborn charts (like histograms and heatmaps) to spot patterns and inspect distributions myself.</li>
    <li><strong>Presentation charts:</strong> Clean, styled plots with custom titles, adjusted limits, and text annotations to make the main takeaway clear to a viewer.</li>
  </ul>'''
}

def slugify(s):
    s = s.lower().replace('&amp;', 'and').replace('&', 'and').replace(':', '')
    s = re.sub(r'[^a-z0-9\s-]', '', s)
    s = re.sub(r'[\s-]+', '-', s).strip('-')
    return s

def parse_part(part_num, part_text):
    sections = re.split(r'\n### ', part_text)
    
    # Collect sections for TOC
    toc_links = []
    for sec in sections[1:]:
        lines = sec.split('\n')
        sec_title = lines[0].strip()
        anchor_id = slugify(sec_title)
        toc_links.append((sec_title, anchor_id))
        
    toc_html = []
    toc_html.append('  <div class="sidebar-toc" id="sidebar-toc">')
    toc_html.append('    <div class="toc-header">')
    toc_html.append('      <span class="toc-title">Table of Contents</span>')
    toc_html.append('      <button class="toc-toggle" id="toc-toggle-btn" aria-label="Toggle TOC">')
    toc_html.append('        <span class="toc-toggle-icon">&minus;</span>')
    toc_html.append('      </button>')
    toc_html.append('    </div>')
    toc_html.append('    <div class="toc-body">')
    toc_html.append('      <ul class="toc-list">')
    for title, anchor in toc_links:
        toc_html.append(f'        <li><a href="#{anchor}">{title}</a></li>')
    toc_html.append('      </ul>')
    toc_html.append('    </div>')
    toc_html.append('  </div>')
    toc_html.append('''  <script>
    document.getElementById('toc-toggle-btn').addEventListener('click', () => {
      const toc = document.getElementById('sidebar-toc');
      const icon = document.querySelector('.toc-toggle-icon');
      toc.classList.toggle('collapsed');
      if (toc.classList.contains('collapsed')) {
        icon.innerHTML = '&#43;';
      } else {
        icon.innerHTML = '&minus;';
      }
    });
  </script>''')
    toc_html_str = '\n'.join(toc_html)
    
    html_out = []
    # Prepend the walkthrough introduction and Table of Contents
    html_out.append(walkthrough_intro[part_num])
    html_out.append(toc_html_str)
    
    for sec in sections[1:]:
        lines = sec.split('\n')
        sec_title = lines[0].strip()
        sec_body = '\n'.join(lines[1:])
        anchor_id = slugify(sec_title)
        
        html_out.append(f"  <hr/>")
        html_out.append(f"  <h2 id=\"{anchor_id}\">{sec_title}</h2>")
        
        items = re.split(r'\n#### ', sec_body)
        sec_intro = items[0].strip()
        if sec_intro:
            for p in sec_intro.split('\n\n'):
                p = p.strip()
                if p and not p.startswith('**File Path**') and not p.startswith('---'):
                    html_out.append(f"  <p>{p}</p>")
                    
        for item in items[1:]:
            item_lines = item.split('\n')
            item_title = item_lines[0].strip()
            item_body = '\n'.join(item_lines[1:])
            
            # Check if this item should render as a chart block in Part 4
            is_chart = False
            img_file = ""
            img_desc = ""
            if part_num == 4:
                # Clean up the key string for lookup
                clean_title = re.sub(r'^\d+\.\s*', '', item_title).strip()
                if clean_title in images_map:
                    is_chart = True
                    img_file, img_desc = images_map[clean_title]
            
            if is_chart:
                html_out.append(f'  <div class="chart-block">')
                html_out.append(f'    <h3>{item_title}</h3>')
                
                # Now extract code
                item_lines_body = item_body.split('\n')
                in_code = False
                code_lines = []
                for line in item_lines_body:
                    line_strip = line.strip()
                    if line_strip.startswith("```"):
                        if not in_code:
                            in_code = True
                            code_lines = []
                        else:
                            in_code = False
                            code_text = '\n'.join(code_lines)
                            html_out.append(f"    <pre><code>{code_text}</code></pre>")
                    else:
                        if in_code:
                            code_lines.append(line)
                        else:
                            if line_strip and not line_strip.startswith('* **Output'):
                                line_formatted = re.sub(r'\*\*([^*]+)\*\*', r'<strong>\1</strong>', line)
                                line_formatted = re.sub(r'`([^`]+)`', r'<code>\1</code>', line_formatted)
                                html_out.append(f"    <p>{line_formatted.strip()}</p>")
                
                html_out.append(f'    <div class="chart-output">')
                html_out.append(f'      <img src="assets/charts/{img_file}" alt="{item_title}"/>')
                html_out.append(f'    </div>')
                html_out.append(f'    <div class="chart-label"><strong>Interpretation:</strong> {img_desc}</div>')
                html_out.append(f'  </div>')
            else:
                html_out.append(f"  <h3>{item_title}</h3>")
                item_lines_body = item_body.split('\n')
                in_code = False
                code_lines = []
                code_lang = ""
                output_label = "Output"
                
                for line in item_lines_body:
                    line_strip = line.strip()
                    if line_strip.startswith("```"):
                        if not in_code:
                            in_code = True
                            code_lang = line_strip[3:]
                            code_lines = []
                        else:
                            in_code = False
                            code_text = '\n'.join(code_lines)
                            if code_lang == "python":
                                html_out.append(f"  <pre><code>{code_text}</code></pre>")
                            elif code_lang == "text":
                                html_out.append(f'  <div class="jup-out">')
                                html_out.append(f'    <div class="jup-out-label">{output_label}</div>')
                                safe_output = code_text.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')
                                html_out.append(f'    <div class="jup-text">{safe_output}</div>')
                                html_out.append(f'  </div>')
                    else:
                        if in_code:
                            code_lines.append(line)
                        else:
                            out_match = re.match(r'^\*\s+\*\*Output\s*-\s*([^*]+)\*\*:', line_strip)
                            out_match_simple = re.match(r'^\*\s+\*\*Output\*\*:', line_strip)
                            if out_match:
                                output_label = f"Output - {out_match.group(1).strip()}"
                            elif out_match_simple:
                                output_label = "Output"
                            else:
                                if line_strip:
                                    line_formatted = re.sub(r'\*\*([^*]+)\*\*', r'<strong>\1</strong>', line)
                                    line_formatted = re.sub(r'`([^`]+)`', r'<code>\1</code>', line_formatted)
                                    html_out.append(f"  <p>{line_formatted.strip()}</p>")
                                
    return '\n\n'.join(html_out)

takeaways = {
    1: '  <div class="about-box" style="margin-top:2.5rem; margin-bottom:2.5rem; max-width: 100%;">\n    <p><strong>Part 1 Takeaway:</strong> Getting comfortable with Python basics made me realize how tedious it is to manually handle and query raw lists. It helped me understand why libraries like Pandas are so valuable - doing everything in base Python loops is slow and easily leads to bugs.</p>\n  </div>',
    2: '  <div class="about-box" style="margin-top:2.5rem; margin-bottom:2.5rem; max-width: 100%;">\n    <p><strong>Part 2 Takeaway:</strong> Messy data is the norm. I learned that you cannot just load a dataset and immediately start plotting it. You have to spend a significant amount of time checking for null values, fixing formatting, and making logical decisions on how to fill missing entries without biasing the dataset.</p>\n  </div>',
    3: '  <div class="about-box" style="margin-top:2.5rem; margin-bottom:2.5rem; max-width: 100%;">\n    <p><strong>Part 3 Takeaway:</strong> Visual inspections can be misleading. Calculating statistical metrics like Z-scores and correlation coefficients gives you concrete numbers to back up your assumptions, ensuring your business conclusions are mathematically sound.</p>\n  </div>',
    4: '  <div class="about-box" style="margin-top:2.5rem; margin-bottom:2.5rem; max-width: 100%;">\n    <p><strong>Part 4 Takeaway:</strong> There is a big difference between a quick chart you use to check your own work and a styled chart you show to a client. Customizing labels, adjusting axes, and adding text annotations ensure that the main business insight is immediately clear without needing a separate explanation.</p>\n  </div>'
}

for part_num in range(1, 5):
    part_html = parse_part(part_num, parts_raw[part_num])
    
    file_paths = [
        f"/Users/jevanhava/Documents/Project/Portofolio/Preview/python-part{part_num}.html",
        f"/Users/jevanhava/Documents/Project/Portofolio/python-part{part_num}.html"
    ]
    for file_path in file_paths:
        with open(file_path, "r", encoding="utf-8") as f:
            html_content = f.read()
            
        pattern = re.compile(r'(<div class="part-page">).*?(<div class="flowchart">)', re.DOTALL)
        replacement = f'\\1\n\n{part_html}\n\n{takeaways[part_num]}\n\n  \\2'
        new_html = pattern.sub(replacement, html_content)
        
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(new_html)
        print(f"Generated and updated {file_path}")
