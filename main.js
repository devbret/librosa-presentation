const width = 700,
  height = 600,
  radius = 250;

const svg = d3
  .select("#radar")
  .attr("viewBox", `0 0 ${width} ${height}`)
  .append("g")
  .attr("transform", `translate(${width / 2},${height / 2})`);

const features = [
  "tempo",
  "avg_beat_time",
  "avg_chroma_intensity",
  "avg_mfcc_value",
];

const angleSlice = (2 * Math.PI) / features.length;

d3.json("audio_feature_summary.json").then((data) => {
  const extentByFeature = new Map(
    features.map((f) => [f, d3.extent(data, (d) => Math.abs(d[f]))]),
  );

  const normalize = (f, v) => {
    const [min, max] = extentByFeature.get(f);
    if (max === min) return 0.5;
    return (Math.abs(v) - min) / (max - min);
  };

  const normalized = data.map((d) => ({
    file: d.file,
    values: features.map((f) => ({
      axis: f,
      value: normalize(f, d[f]),
    })),
  }));

  features.forEach((feature, i) => {
    const angle = i * angleSlice;
    const x = radius * Math.cos(angle - Math.PI / 2);
    const y = radius * Math.sin(angle - Math.PI / 2);

    svg
      .append("line")
      .attr("x1", 0)
      .attr("y1", 0)
      .attr("x2", x)
      .attr("y2", y)
      .attr("stroke", "#ccc");

    svg
      .append("text")
      .attr("x", x * 1.12)
      .attr("y", y * 1.12)
      .attr("text-anchor", "middle")
      .attr("class", "axisLabel")
      .text(feature);
  });

  const radarLine = d3
    .lineRadial()
    .radius((d) => d.value * radius)
    .angle((d, i) => i * angleSlice)
    .curve(d3.curveLinearClosed);

  const color = d3.scaleOrdinal(d3.schemeCategory10);

  normalized.forEach((entry, idx) => {
    svg
      .append("path")
      .datum(entry.values)
      .attr("d", radarLine)
      .attr("class", "radarStroke")
      .attr("stroke", color(idx));

    svg
      .append("path")
      .datum(entry.values)
      .attr("d", radarLine)
      .attr("class", "radarArea")
      .attr("fill", color(idx));
  });

  normalized.forEach((entry, idx) => {
    entry.values.forEach((d, i) => {
      const angle = i * angleSlice - Math.PI / 2;
      const r = d.value * radius;
      const x = r * Math.cos(angle);
      const y = r * Math.sin(angle);

      svg
        .append("circle")
        .attr("cx", x)
        .attr("cy", y)
        .attr("r", 3)
        .attr("fill", color(idx));
    });
  });
});
