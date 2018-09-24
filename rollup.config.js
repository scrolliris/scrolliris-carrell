import fs from 'fs';
import path from 'path';

import buble from 'rollup-plugin-buble';
import commonjs from 'rollup-plugin-commonjs';
import css from 'rollup-plugin-css-only';
import csso from 'csso';
import hash from 'rollup-plugin-hash';
import hasha from 'hasha';
import nodeResolve from 'rollup-plugin-node-resolve';
import stylus from 'rollup-plugin-stylus-compiler';
import { terser } from 'rollup-plugin-terser';

let root_dir = __dirname
  , assets_dir = path.join(root_dir, 'rapperswil_jona', 'assets')
  , static_dir = path.join(root_dir, 'static')
  , inputs = []
  ;

if (process.env.NODE_ENV === 'production') {
  let manifestJSON = path.join(static_dir, 'manifest.json');
  let hashaOptions = {
      algorithm: 'sha1'
    , replace: false
  };

  inputs = [{
    input: path.join(assets_dir, 'index.js')
  , output: [{
      file: path.join(static_dir, 'index.min.js')
    , format: 'iife'
    , sourcemap: false
    , globals: ['fontfaceobserver']
    }]
  , plugins: [
      nodeResolve({jsnext: true, module: true})
    , stylus()
    , css({
        output: function(styles, styleNodes) {
          fs.writeFileSync(
            path.join(static_dir, 'index.min.css')
          , csso.minify(styles).css
          );
        }
      })
    , buble()
    , commonjs()
    , terser()
    , hash({
        ...hashaOptions
      , manifest: manifestJSON
      , manifestKey: 'index.js'
      , dest: path.join(static_dir, 'index.min.[hash].js')
      , callback: (hashedJsFile) => {
          // delete unnecessary js file
          let jsFile = path.join(static_dir, 'index.min.js');
          fs.unlinkSync(jsFile);

          console.log(hashedJsFile);

          // update the key in manifest.json
          let manifest = fs.readFileSync(manifestJSON);
          let contents = JSON.parse(manifest);
          delete contents[jsFile];
          contents['index.js'] = hashedJsFile;
          fs.writeFileSync(manifestJSON, JSON.stringify(contents));
        }
      })
    , {
        name: 'hash (css)'
      , onwrite: (_bundle, _data) => {
          let cssFile = path.join(static_dir, 'index.min.css');

          // rename min.css using [hash]
          let cssData = fs.readFileSync(cssFile, 'utf8');
          let hash = hasha(cssData, hashaOptions);
          let hashedCssFile = cssFile.replace(/\.css$/, `.${hash}.css`);
          fs.renameSync(cssFile,  hashedCssFile);

          console.log(hashedCssFile);

          // add css entry into manifest.json
          let manifest = fs.readFileSync(manifestJSON);
          let contents = JSON.parse(manifest);
          contents['index.css'] = hashedCssFile;
          fs.writeFileSync(manifestJSON, JSON.stringify(contents));
        }
      }
    ]
  }];
} else {
  inputs = [{
    input: path.join(assets_dir, 'index.js')
  , output: {
      file: path.join(static_dir, 'index.js')
    , format: 'iife'
    , sourcemap: true
    , globals: ['fontfaceobserver']
    }
  , plugins: [
      nodeResolve({jsnext: true, module: true})
    , stylus()
    , css()
    , buble()
    , commonjs()
    ]
  }];
}

export default inputs
