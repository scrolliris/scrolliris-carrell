import buble from 'rollup-plugin-buble';
import nodeResolve from 'rollup-plugin-node-resolve';
import { terser } from 'rollup-plugin-terser';

export default [{
  input: './rapperswil_jona/assets/index.js'
, output: {
    file: './static/index.js'
  , format: 'es'
  , sourcemap: true
  }
, plugins: [
    nodeResolve({
      jsnext: true
    })
  , buble()
  ]
, external(id) {
    return !/^[./]/.test(id)
  }
}, {
  input: './rapperswil_jona/assets/index.js'
, output: [{
    file: './static/index.min.js'
  , format: 'es'
  , sourcemap: false
  }]
, plugins: [
    nodeResolve({
      jsnext: true
    })
  , buble()
  , terser()
  ]
, external(id) {
    return !/^[./]/.test(id)
  }
}]
