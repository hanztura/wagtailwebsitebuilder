Vue.component('modal-card', {
  props: [
    'message',
    'title',
    'showModal',
  ],
  data: () => {
    return {}
  },
  methods: {
    closeModal: function () {
      console.log('hahaha')
      this.$emit('close-modal');
    }
  },
  name: 'ModalCard',
  delimiters: ['[[', ']]'],
  template: `
    <div :class="{'modal': true, 'is-active': showModal}">
      <div class="modal-background" @click.prevent="closeModal"></div>
      <div class="modal-card">
        <div class="modal-card-head">
          <p class="modal-card-title">[[ title ]]</p>
          <button type="button" class="delete" aria-label="close" @click.prevent="closeModal"></button>
        </div>
        <div class="modal-card-body">
          <p>[[ message ]]</p>
        </div>
        <div class="modal-card-foot">
          <button type="button" class="button " @click.prevent="closeModal">Close</button>
        </div>
      </div>
    </div>
  `
});
