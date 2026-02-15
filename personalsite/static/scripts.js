// Modern vanilla JavaScript - no jQuery needed

// Toggle visibility of element
function togglehide(elemId) {
  const elem = document.getElementById(elemId);
  if (!elem) return;
  
  elem.style.display = elem.style.display === 'none' ? 'block' : 'none';
}

// Smooth scroll to anchor (for Projects link)
document.addEventListener('DOMContentLoaded', () => {
  const links = document.querySelectorAll('a[href^="#"]');
  
  links.forEach(link => {
    link.addEventListener('click', (e) => {
      const href = link.getAttribute('href');
      if (href === '#') return;
      
      e.preventDefault();
      const target = document.querySelector(href);
      
      if (target) {
        target.scrollIntoView({
          behavior: 'smooth',
          block: 'start'
        });
      }
    });
  });
});

// Gallery: Simple image lazy loading hint
if ('loading' in HTMLImageElement.prototype) {
  const images = document.querySelectorAll('img.lazy');
  images.forEach(img => {
    img.src = img.dataset.src;
  });
}

// Tag Visualization - Force-directed graph
document.addEventListener('DOMContentLoaded', () => {
  const canvas = document.getElementById('tag-canvas');
  if (!canvas || typeof tagData === 'undefined') return;
  
  const container = document.getElementById('tag-visualization');
  const rect = container.getBoundingClientRect();
  
  canvas.width = rect.width;
  canvas.height = 500;
  
  const ctx = canvas.getContext('2d');
  const width = canvas.width;
  const height = canvas.height;
  
  // Physics parameters
  const centerForce = 0.02;
  const repelForce = 500;
  const linkForce = 0.01;
  const damping = 0.85;
  const minRadius = 8;
  const maxRadius = 30;
  
  // Find max count for scaling
  const maxCount = Math.max(...tagData.nodes.map(n => n.count));
  
  // Initialize nodes with physics
  const nodes = tagData.nodes.map(n => ({
    id: n.id,
    count: n.count,
    radius: minRadius + (n.count / maxCount) * (maxRadius - minRadius),
    x: Math.random() * width,
    y: Math.random() * height,
    vx: 0,
    vy: 0,
    hovered: false
  }));
  
  const links = tagData.links;
  
  // Build node map for quick lookup
  const nodeMap = new Map(nodes.map(n => [n.id, n]));
  
  // Mouse tracking
  let mouseX = 0;
  let mouseY = 0;
  let hoveredNode = null;
  
  canvas.addEventListener('mousemove', (e) => {
    const rect = canvas.getBoundingClientRect();
    mouseX = e.clientX - rect.left;
    mouseY = e.clientY - rect.top;
    
    hoveredNode = null;
    for (const node of nodes) {
      const dx = mouseX - node.x;
      const dy = mouseY - node.y;
      const dist = Math.sqrt(dx * dx + dy * dy);
      node.hovered = dist < node.radius;
      if (node.hovered) hoveredNode = node;
    }
  });
  
  canvas.addEventListener('click', () => {
    if (hoveredNode) {
      window.location.href = `/articles/?tags=${hoveredNode.id}`;
    }
  });
  
  canvas.style.cursor = 'default';
  canvas.addEventListener('mousemove', () => {
    canvas.style.cursor = hoveredNode ? 'pointer' : 'default';
  });
  
  // Physics simulation
  function simulate() {
    // Apply forces
    for (const node of nodes) {
      // Center attraction
      const dx = width / 2 - node.x;
      const dy = height / 2 - node.y;
      node.vx += dx * centerForce;
      node.vy += dy * centerForce;
      
      // Node repulsion
      for (const other of nodes) {
        if (node === other) continue;
        const dx = node.x - other.x;
        const dy = node.y - other.y;
        const dist = Math.sqrt(dx * dx + dy * dy) + 1;
        const force = repelForce / (dist * dist);
        node.vx += (dx / dist) * force;
        node.vy += (dy / dist) * force;
      }
    }
    
    // Link forces
    for (const link of links) {
      const source = nodeMap.get(link.source);
      const target = nodeMap.get(link.target);
      if (!source || !target) continue;
      
      const dx = target.x - source.x;
      const dy = target.y - source.y;
      const dist = Math.sqrt(dx * dx + dy * dy);
      const force = (dist - 80) * linkForce * link.weight;
      
      source.vx += (dx / dist) * force;
      source.vy += (dy / dist) * force;
      target.vx -= (dx / dist) * force;
      target.vy -= (dy / dist) * force;
    }
    
    // Update positions
    for (const node of nodes) {
      node.vx *= damping;
      node.vy *= damping;
      node.x += node.vx;
      node.y += node.vy;
      
      // Keep in bounds
      node.x = Math.max(node.radius, Math.min(width - node.radius, node.x));
      node.y = Math.max(node.radius, Math.min(height - node.radius, node.y));
    }
  }
  
  // Render
  function render() {
    ctx.clearRect(0, 0, width, height);
    
    // Draw links
    ctx.strokeStyle = 'rgba(59, 130, 246, 0.1)';
    ctx.lineWidth = 1;
    for (const link of links) {
      const source = nodeMap.get(link.source);
      const target = nodeMap.get(link.target);
      if (!source || !target) continue;
      
      ctx.beginPath();
      ctx.moveTo(source.x, source.y);
      ctx.lineTo(target.x, target.y);
      ctx.stroke();
    }
    
    // Draw nodes
    for (const node of nodes) {
      ctx.beginPath();
      ctx.arc(node.x, node.y, node.radius, 0, Math.PI * 2);
      
      if (node.hovered) {
        ctx.fillStyle = '#3b82f6';
        ctx.fill();
        ctx.strokeStyle = '#60a5fa';
        ctx.lineWidth = 2;
        ctx.stroke();
      } else {
        ctx.fillStyle = 'rgba(59, 130, 246, 0.6)';
        ctx.fill();
        ctx.strokeStyle = 'rgba(59, 130, 246, 0.8)';
        ctx.lineWidth = 1;
        ctx.stroke();
      }
      
      // Draw label
      ctx.fillStyle = '#e8e8e8';
      ctx.font = `${Math.min(12, node.radius * 0.6)}px Inter, sans-serif`;
      ctx.textAlign = 'center';
      ctx.textBaseline = 'middle';
      
      if (node.radius > 15 || node.hovered) {
        ctx.fillText(node.id, node.x, node.y);
      }
    }
    
    // Draw hover label
    if (hoveredNode) {
      ctx.fillStyle = 'rgba(17, 17, 17, 0.9)';
      ctx.strokeStyle = '#3b82f6';
      ctx.lineWidth = 1;
      const text = `${hoveredNode.id} (${hoveredNode.count})`;
      ctx.font = '14px Inter, sans-serif';
      const metrics = ctx.measureText(text);
      const padding = 8;
      const boxWidth = metrics.width + padding * 2;
      const boxHeight = 24;
      const boxX = hoveredNode.x - boxWidth / 2;
      const boxY = hoveredNode.y - hoveredNode.radius - boxHeight - 10;
      
      ctx.beginPath();
      ctx.roundRect(boxX, boxY, boxWidth, boxHeight, 4);
      ctx.fill();
      ctx.stroke();
      
      ctx.fillStyle = '#e8e8e8';
      ctx.textAlign = 'center';
      ctx.textBaseline = 'middle';
      ctx.fillText(text, hoveredNode.x, boxY + boxHeight / 2);
    }
  }
  
  // Animation loop
  let running = true;
  let iterations = 0;
  function animate() {
    if (iterations < 300) {
      simulate();
      iterations++;
    }
    render();
    if (running) requestAnimationFrame(animate);
  }
  
  animate();
});
