export function applyDiscount(total, percent) {
  if (percent <= 0 || percent >= 100) {
    return total;
  }
  return Math.round(total * (100 - percent)) / 100;
}

export function bestDiscount(candidates) {
  return candidates.reduce((best, next) => (next > best ? next : best), 0);
}
