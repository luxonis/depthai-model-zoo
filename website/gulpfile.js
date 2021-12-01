const gulp = require('gulp');
const shell = require('gulp-shell');
const filter = require('gulp-filter-each');
const fileInclude = require('gulp-file-include');
const sass = require('gulp-sass');
const autoprefixer = require('gulp-autoprefixer');

const port = 3000;

gulp.task('build-template', async function() {
  await gulp.src('src/template/*.html')
    .pipe(filter(content => content.match(/<html>/gi)))
    .pipe(fileInclude({
      prefix: '@@',
      basepath: '@file'
    }))
    .pipe(gulp.dest('./web'));
});

gulp.task('build-scss', async function() {
  await gulp.src('src/scss/*.scss')
    .pipe(sass().on('error', sass.logError))
    .pipe(autoprefixer({ cascade: false }))
    .pipe(gulp.dest('./web/css'));
});

gulp.task('copy-css', async function() {
  await gulp.src('src/css/*.css')
    .pipe(autoprefixer({ cascade: false }))
    .pipe(gulp.dest('./web/css'));
});

gulp.task('copy-js', async function() {
  await gulp.src('src/js/**/*.*')
    .pipe(gulp.dest('./web/js'));
});

gulp.task('copy-assets', async function() {
  await gulp.src('src/assets/*.*')
    .pipe(gulp.dest('./web/assets'));
});

gulp.task('build', gulp.series('build-template', 'build-scss', 'copy-css', 'copy-js', 'copy-assets'));

gulp.task('watch', function(resolve) {
  const watchSrcFolders = ['src/template/**', 'src/scss/**', 'src/css/**', 'src/js/**'/*, 'src/assets/**'*/];
  gulp.watch(watchSrcFolders, gulp.series('build'));
  resolve();
});

// demo server
gulp.task('server', gulp.series(shell.task([
  `http-server --port ${port} ./web -c 0`
])));

// dev server
gulp.task('dev', gulp.series('build', 'watch', 'server'));

gulp.task('deploy-init', gulp.series(shell.task([
  'firebase init'
])));

gulp.task('deploy', gulp.series('build', shell.task([
  'firebase deploy'
])));
