<template>
	<div id="app">
		<!--img alt="Vue logo" src="./assets/logo.png"-->
		<ul>
			<li v-for="item, index in my_dirs" :key="index">
				<button class="my_button" type="button" v-on:click="onSwitch(index)">{{item}}</button>
			</li>
		</ul>
		<br>单击图片进行切换</br>
		<div v-if="my_dir!=''" @click="onClick" class="my_pic_div">
			<!--button type="button" v-on:click="onClick()">点击切换</button-->
			<img height="700" v-bind:src="my_pic"/>
		</div>
		<!--HelloWorld msg="Welcome to Your Vue.js App"/-->
	</div>
</template>

<script>
	//import HelloWorld from './components/HelloWorld.vue'
	//import Ping from './components/ping.vue'
	import axios from 'axios';
	
	export default {
		name: 'app',
		components: {
			//HelloWorld,
		},
		data: function(){
			return {
				my_pic: './static/w2.jpg',
				my_pics: [],
				my_dirs: [],
				my_dir: '',
				idx: 0
			}
		},
		methods: {
			getDirList() {
				const path = 'http://192.168.3.7:5000/dir';
				axios.get(path, null, { params: {root:'static'}})
				.then((res) => {
					this.my_dirs = res.data;
				})
				.catch((error) => {
					// eslint-disable-next-line
					console.error(error);
				});
			},
			getPicList(pic_dir) {
				const path = 'http://192.168.3.7:5000/folder/'+pic_dir;
				axios.get(path, null, { params: {root:pic_dir}})
				.then((res) => {
					this.my_pics = res.data;
				})
				.catch((error) => {
					// eslint-disable-next-line
					console.error(error);
				});
			},
			onClick() {
				console.log('pic num: '+this.my_pics.length);
				if(this.my_pics.length > 0) {
					var my_pic_str = this.my_pics[this.idx];
					console.log('my_pics[' + this.idx + ']: ' + my_pic_str);
					console.log('my_pic_str: '+my_pic_str);
					this.my_pic = require('./static/'+this.my_dir+'/'+my_pic_str);
					this.idx = this.idx+1;
					if(this.idx >= this.my_pics.length) {
						this.idx = 0;
					}
				}
			},
			onSwitch(index) {
				this.my_dir = this.my_dirs[index];
				console.log(index +" : "+this.my_dir);
				this.getPicList(this.my_dir);
			}
		},
		created() {
			this.getDirList();
			//this.onClick();
		},
	}
</script>

<style>
	#app {
		font-family: Avenir, Helvetica, Arial, sans-serif;
		-webkit-font-smoothing: antialiased;
		-moz-osx-font-smoothing: grayscale;
		text-align: center;
		color: #2c3e50;
		margin-top: 60px;
	}
	.my_button{font-size:40px; width: 200px; margin:10px 10px 10px 10px;}
	.my_pic_div{text-align:center}
	li{ float:left; list-style:none}
</style>
