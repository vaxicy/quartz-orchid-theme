
// Quartz Orchid Theme - quartz white, grey orchid and pale gold
import { readFile } from 'node:fs/promises';

const QUARTZ_PALETTE = {
  orchid: '#B9A7CC',
  orchidDeep: '#8C76A3',
  gold: '#D6C49E',
  quartz: '#F5F2F5',
  mist: '#B0BCC8',
};

export class GemCutter {
  constructor(bench = 'Quartz bench') {
    this.bench = bench;
    this.palette = QUARTZ_PALETTE;
  }

  /** Mix two mineral tones into a muted shade. */
  mix(from, to, ratio = 0.5) {
    const parse = (hex) =>
      [1, 3, 5].map((i) => parseInt(hex.slice(i, i + 2), 16));
    const [a, b] = [parse(from), parse(to)];
    const channel = (value, i) =>
      Math.round(value * (1 - ratio) + b[i] * ratio);
    const toHex = (value) => value.toString(16).padStart(2, '0');
    return '#' + a.map(channel).map(toHex).join('');
  }

  async readSpec(file) {
    const content = await readFile(file, 'utf8');
    const steps = content.split('\n').filter(Boolean);
    return {
      bench: this.bench,
      tones: Object.keys(this.palette).length,
      steps: steps.length,
      content,
    };
  }
}

const cutter = new GemCutter();
const wash = cutter.mix(QUARTZ_PALETTE.orchid, QUARTZ_PALETTE.quartz);

console.log(`wash shade: ${wash}`);
